from django.db import models
from django.forms import ModelForm

# Create your models here.
class Blog(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text', max_length=2048)
    captured_date = models.DateField(auto_now_add=True)

class Comments(models.Model):
    name = models.CharField('Name', max_length=200,null=True, blank=True)
    email = models.EmailField('email', null=True, blank=True)
    captured_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField('Comment', max_length=2048)
    blog = models.ForeignKey(Blog)

#class CommentsForm(ModelForm):
#    '''The Comments Form '''
#    class Meta:
#            model = Comments

#class Person(models.Model):
#    name = models.CharField('Name', max_length=200)
#    surname = models.CharField('Surname', max_length=200)
#    blogs = models.ManyToManyField(Blog, blank=True)
#
#    def __unicode__(self):
#        return self.name
#
class Purcharser(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    reference = models.CharField('Reference', max_length=50)
    street = models.CharField('Street', max_length=200)
    surburb = models.CharField('Surburb', max_length=200)
    city = models.CharField('City', max_length=200)
    province = models.CharField('Province', max_length=50)
    pcode = models.IntegerField('Postal code')
    email = models.EmailField('email', null=True, blank=True)

class Event(models.Model):
    name = models.CharField('Name', max_length=50)
    datepicker = models.DateField('Date')
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_details = models.TextField(max_length=500)


class Photos(models.Model):
    photo_name = models.ImageField(upload_to='media/%Y/%m/%d')
    event_photo = models.ForeignKey(Event)
#class PurchaserForm(ModelForm):
#    '''The Supporter Form '''
#    class Meta:
#            model = Purcharser
#            
#            