from django.utils import timezone
from django.db import models
import datetime
from cloudinary.models import CloudinaryField

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')    

    def __unicode__(self): 
        return self.question    

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self): 
        return self.choice_text

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    created = models.DateTimeField('Date account created', auto_now_add=True)
    email = models.EmailField()
    birth_date = models.DateField()
    profile_picture = CloudinaryField('image')
    class Meta:
        abstract = True

class Musician(User):
    pass

class Reviewer(User):
    pass
    
class Review(User):
    artist = models.ForeignKey(Musician)
    reviewer = models.ForeignKey(Reviewer)        

    title = models.CharField(max_length=100)
    body = models.TextField()
    release_date = models.DateField()
    num_stars = models.IntegerField()
