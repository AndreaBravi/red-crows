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
    profile_picture = CloudinaryField('image', null=True, blank=True)
    class Meta:
        abstract = True

class Musician(User):
    pass

class Reviewer(User):
    pass

class MusicianProduct(models.Model):
    PRODUCT_TYPES = (('S', 'Song'), 
                     ('A', 'Album'),
                     ('C', 'Collection'))
    musician = models.ForeignKey(Musician)    
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    description = models.TextField()
    product_picture = CloudinaryField('image', null=True, blank=True)

class Review(models.Model):
    musician = models.ForeignKey(Musician)
    reviewer = models.ForeignKey(Reviewer)        
    product = models.ForeignKey(MusicianProduct)
    title = models.CharField(max_length=100)
    body = models.TextField()
    release_date = models.DateField()
    num_stars = models.IntegerField()

