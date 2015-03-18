from django.utils import timezone
from django.db import models
import datetime
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


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

class AbstractUser(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(User)        
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    birth_date = models.DateField()        
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(unique=True)
    # bank account
    created = models.DateTimeField('Date account created', auto_now_add=True)    
    profile_picture = CloudinaryField('image', blank=True, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    

class Musician(AbstractUser):
    number_reviews_received = models.PositiveSmallIntegerField(blank=True, null=True)
    number_products = models.PositiveSmallIntegerField(blank=True, null=True)
    artist_name = models.CharField(max_length=50, blank=True)

class Reviewer(AbstractUser):
    number_reviews_performed = models.PositiveSmallIntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True)

class Music(models.Model):
    PRODUCT_TYPES = (('S', 'Song'), 
                     ('A', 'Album'),
                     ('C', 'Collection'))
    musician = models.ForeignKey(Musician)    
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField('Date product created', auto_now_add=True)
    product_picture = CloudinaryField('image', blank=True, null=True)
    average_score = models.PositiveSmallIntegerField(blank=True, null=True)
    number_reviews_received = models.PositiveSmallIntegerField(blank=True, null=True)
    def __unicode__(self):
        return u'%s - %s' % (self.musician, self.title)
    
class Review(models.Model):
    musician = models.ForeignKey(Musician)
    reviewer = models.ForeignKey(Reviewer)        
    product = models.ForeignKey(Music)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created = models.DateTimeField('Date review created', auto_now_add=True)
    score = models.PositiveSmallIntegerField()
    def __unicode__(self):
        return u'%s: %s' % (self.reviewer, self.product)
