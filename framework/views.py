from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from framework.models import Choice, Poll, Musician, Review, Reviewer

class IndexView2(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))    

class IndexView(generic.DetailView):
    template_name = 'base/index.html'
    
class MusicianView(generic.DetailView):
    model = Musician
    template_name = 'base/musician.html'        

class ReviewerView(generic.DetailView):
    model = Reviewer
    template_name = 'base/reviewer.html'            

class ReviewView(generic.DetailView):
    model = Review
    template_name = 'base/review.html'                