from django.forms import ModelForm
from framework.models import Musician, Reviewer


class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'birth_date', 'artist_name', 
                  'description', 'website', 'profile_picture']

class ReviewerForm(ModelForm):
    class Meta:
        model = Reviewer
        fields = ['first_name', 'last_name', 'birth_date', 'job_title', 
                  'description', 'website', 'profile_picture']