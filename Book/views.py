# Create your views here.

from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms as forms
from django.template import RequestContext

from django.core.mail import EmailMessage
from tinymce.widgets import TinyMCE
from Book.models import Blog
from Book.models import Comments
from Book.models import Event
from Book.models import Photos

from django.http import HttpResponse
from django.core import serializers

from django.utils import simplejson  
from django.utils.functional import Promise  
from django.utils.encoding import force_unicode 
from datetime import datetime
from django.core import serializers


#***********AJAX**EVENTS*********
#here is some magic. We need to write custom JSON encoder, since sometimes  
#serializing lazy strings can cause errors.   
#You need to write it only once and then can reuse in any app  
 
class LazyEncoder(simplejson.JSONEncoder):  
    """Encodes django's lazy i18n strings. 
    """  
    def default(self, obj):  
        if isinstance(obj, Promise):  
            return force_unicode(obj)  
        return obj
    
def xhr_test(request):
    if request.is_ajax():
        if request.method == 'GET':
            curr_mont = datetime.now().month
            curr_year = datetime.now().year
            curr_mont_events = Event.objects.filter(datepicker__month=curr_mont,datepicker__year=curr_year)
            data = serializers.serialize('json', curr_mont_events)
            message = curr_mont_events
        #    result = simplejson.dumps({  
        #    "message": message,  
        #    "type": type,  
        #}, cls=LazyEncoder)
            print message
        elif request.method == 'POST':
            message = "This is an XHR POST request"
            # Here we can access the POST data
            print request.POST
    else:
        message = "No XHR"    
    return HttpResponse(data, mimetype='application/javascript')
#***********END**AJAX**EVENTS*********


#**********Forms********
class CommentsForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':'4','cols':'60'}))


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message= forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 4}))
    
#**********End of Forms********

#********Events - Calculate- (home and books calendar)
event_count = Event.objects.count()


#********End of Events - Calculate#
def index(request):
    '''The home page '''
    event_count = Event.objects.count()
    
    #********************************
    #
    eveny = Event.objects.all()
    
    photos = Photos.objects.all()
    #for i in photos:
        #print i.__dict__
    
    for i in eveny:
        print i.__dict__
        print '+' * 20
        
        for x in i.photos_set.all():
            print x.__dict__ 
        print '+' * 20

    #print event_count
    #***************************
    request.session['Lunga'] = 'Baliowe'
    return render_to_response('home.html',{'event_count':event_count},context_instance = RequestContext(request))
    
def blog(request,title):
    #Need to store extra field on the blog for the url - The New Blog - the-new-blog
    blog = get_object_or_404(Blog, title=title.title())
    comment_form = CommentsForm()
    return render_to_response('Blog/blog_details.html',{'comment_form':comment_form,
                                                        'comments_list':blog.comments_set.all().order_by('captured_date'),
                                                        'blog':blog})
def comments(request,title):
    blog = get_object_or_404(Blog, title=title.title())
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            blog_comment = Comments(name=request.POST['name'],email=request.POST['email'],
                               comment=request.POST['comment'], blog = get_object_or_404(Blog, title=title.title()))
            blog_comment.save()
            return HttpResponseRedirect('/blog/%s'% title)
    else:
        comment_form = CommentsForm()
    return render_to_response('Blog/blog_details.html',
                              {'comment_form':comment_form,
                               'comments_list':blog.comments_set.all().order_by('captured_date'),
                               'blog':blog})

def contact(request):
    '''Sends an email '''
    success_msg = ''
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            from_email = request.POST['email']
            
            #email_message = EmailMessage(subject, message, from_email, to=['info@kazikungenxakabana.co.za'])
            #email_message.send()
            
            success_msg = '%s messazxzxge was successfully sent, we will be in touch with should yo message require a response' % request.POST['name']
    else:
        contact_form = ContactForm()
        
    return render_to_response('contact.html',{'contact_form': contact_form, 'message':success_msg})
    
def announcements(request):
    announce = get_list_or_404(Announcement)
    return announce