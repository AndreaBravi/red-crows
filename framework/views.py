from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from framework.models import Choice, Poll, Musician, Review, Reviewer, Music 
from framework.forms import MusicianForm, ReviewerForm

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

class IndexView(generic.base.TemplateView):
    template_name = 'base/index.html'    
    
class MusicianView(generic.DetailView):
    model = Musician    
    template_name = 'base/musician.html'     

class MusicView(generic.DetailView):
    model = Music
    template_name = 'base/music.html'           

class ReviewerView(generic.DetailView):
    model = Reviewer
    template_name = 'base/reviewer.html'            

class ReviewView(generic.DetailView):
    model = Review
    template_name = 'base/review.html'

# Create

class CreateMusicianView(generic.edit.CreateView):    
    form_class = MusicianForm
    template_name = 'base/create/createmusician.html'    
    success_url = 'thanks/'
    def post(self, request):
        form = self.form_class(request.POST)
        form.email = request.user.email
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return HttpResponseRedirect(self.success_url)

class CreateReviewerView(generic.edit.CreateView):
    form_class = ReviewerForm
    template_name = 'base/create/createreviewer.html'   
    success_url = 'thanks/'
    def post(self, request):
        form = self.form_class(request.POST)
        form.email = request.user.email
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return HttpResponseRedirect(self.success_url)

class CreateMusicView(generic.edit.CreateView):
    model = Music
    template_name = 'base/create/createmusic.html'
    fields = ['musician', 'product_type', 'title', 'description', 'product_picture']
    success_url = 'thanks/'
    # musician should be auto-populated

class CreateReviewView(generic.edit.CreateView):
    model = Review
    template_name = 'base/create/createreview.html'
    fields = ['musician', 'reviewer', 'product', 'title', 'body', 'score']
    success_url = 'thanks/'
    # reviewer should be auto-populated

# Lists

class ListMusicianView(generic.ListView):
    template_name = 'base/lists/listmusician.html'
    context_object_name = 'musician_list'
    def get_queryset(self):        
        return Musician.objects.order_by('-created')

class ListReviewerView(generic.ListView):
    template_name = 'base/lists/listreviewer.html'
    context_object_name = 'reviewer_list'
    def get_queryset(self):        
        return Reviewer.objects.order_by('-created')

class ListReviewView(generic.ListView):
    template_name = 'base/lists/listreview.html'
    context_object_name = 'review_list'
    def get_queryset(self):        
        return Review.objects.order_by('-created')

class ListMusicView(generic.ListView):
    template_name = 'base/lists/listmusic.html'
    context_object_name = 'music_list'
    def get_queryset(self):        
        return Music.objects.order_by('-created')

# Thanks

class ThanksView(generic.base.TemplateView):    
    template_name = 'base/thanks.html'


