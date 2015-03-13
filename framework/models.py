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
    birth_date = models.DateField()
    artist_name = models.CharField(max_length=50, blank=True)    
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField()
    # bank account
    created = models.DateTimeField('Date account created', auto_now_add=True)    
    profile_picture = CloudinaryField('image', blank=True, null=True)
    class Meta:
        abstract = True
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Musician(User):
    number_reviews_received = models.PositiveSmallIntegerField(blank=True, null=True)
    number_products = models.PositiveSmallIntegerField(blank=True, null=True)

class Reviewer(User):
    number_reviews_performed = models.PositiveSmallIntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True)

class MusicianProduct(models.Model):
    PRODUCT_TYPES = (('S', 'Song'), 
                     ('A', 'Album'),
                     ('C', 'Collection'))
    musician = models.ForeignKey(Musician)    
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    product_picture = CloudinaryField('image', blank=True, null=True)
    average_score = models.PositiveSmallIntegerField(blank=True, null=True)
    def __unicode__(self):
        return u'%s - %s' % (self.musician, self.title)
    
class Review(models.Model):
    musician = models.ForeignKey(Musician)
    reviewer = models.ForeignKey(Reviewer)        
    product = models.ForeignKey(MusicianProduct)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    time_created = models.DateTimeField('Date review created', auto_now_add=True)
    score = models.PositiveSmallIntegerField()
    def __unicode__(self):
        return u'%s: %s' % (self.reviewer, self.product)
