from django import forms
from django.forms import widgets

from framework.models import Musician, Review, Reviewer, Music 
from django.contrib.admin.widgets import AdminDateWidget

# class AbstractUserForm(forms.ModelForm):
#     birth_date = forms.DateField(widget=AdminDateWidget)

class MusicianForm(forms.ModelForm):    
    class Meta:
        model = Musician
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}

class ReviewerForm(forms.ModelForm):    
    class Meta:
        model = Reviewer
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}

