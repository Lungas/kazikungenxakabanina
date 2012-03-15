from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail, create_update
from django import contrib
from Book.models import Blog
from Book.models import Purcharser
from Book.models import Event
from Book.models import Photos
from Book.views import CommentsForm, event_count
from Book.sitemap import BlogSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

comment_form = CommentsForm()

quote_list_info = {
    'queryset' : Blog.objects.all().order_by('-captured_date'),
    'allow_empty' : True,
    #"extra_context" : {"comment_count" : Comments.objects.all()}
    
}

event_add_info = {
    'model' : Event,
    'template_name' : 'Event/event_add.html',
    'post_save_redirect' : '/events/',
}

events_list_info = {
    'queryset' : Event.objects.all().order_by('-datepicker'),
    'template_name' : 'Event/event.html',
    'allow_empty' : True,
    
}
event_detail_info = {
    'queryset' : Event.objects.all(),
    'template_object_name' : 'event',
    'template_name' : 'Event/event_details.html',
}


blog_add_info = {
    'model' : Blog,
    'template_name' : 'Book/blog_add.html',
    'post_save_redirect' : '/blog',
}


purchaser_add_info = {
    'model' : Purcharser,
    'template_name' : 'order.html',
    'post_save_redirect' : '/order/thanks',
}
sitemaps = {
    'person': BlogSitemap,
            }

urlpatterns = patterns('',
                       url(r'^$', 'KaziKungenxaKabaniNa.Book.views.index', name='home'),
                       #url(r'^blog/1/$', 'KaziKungenxaKabaniNa.Book.views.submit_blog'),
                       url(r'^blog/blog_add/$',create_update.create_object, blog_add_info, name='blod_add'),
                       url(r'^blog/(?P<title>\w+)/$', 'KaziKungenxaKabaniNa.Book.views.blog'),
                       url(r'^xhr_test$','KaziKungenxaKabaniNa.Book.views.xhr_test'),
                       url(r'^author/$', direct_to_template, { 'template' : 'about.html'}),
                       url(r'^books/$', direct_to_template, { 'template' : 'books.html',"extra_context":{"event_count":Event.objects.count()}}),
                       url(r'^contact/$', 'KaziKungenxaKabaniNa.Book.views.contact'),
                       #url(r'^order/$', direct_to_template, { 'template' : 'order.html'}),
                       #url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^events/$',list_detail.object_list, events_list_info),
                       url(r'^events/add/$',create_update.create_object, event_add_info),
                       url(r'^events/(\d+)/$',list_detail.object_detail, event_detail_info),
                       url(r'^order/$',create_update.create_object, purchaser_add_info),
                       url(r'^order/thanks/$', direct_to_template, { 'template' : 'ordertx.html'}),
                       url(r'^blog/$', list_detail.object_list, quote_list_info),
                       
                       #url(r'^blog/(?P<object_id>\d+)/$',list_detail.object_detail, blog_detail_info),
                       url(r'^blog/(?P<title>\w+)/comments/$', 'KaziKungenxaKabaniNa.Book.views.comments'),
                       
    # Examples:
    # url(r'^$', 'KaziKungenxaKabaniNa.views.home', name='home'),
    # url(r'^KaziKungenxaKabaniNa/', include('KaziKungenxaKabaniNa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                        {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
#urlpatterns += patterns('',
#    (r'^blog/$', list_detail.object_list, quote_list_info),
#    (r'^blog/blog_add/$',create_update.create_object, blog_add_info),
    #(r'^blog/(?P<object_id>\d+)/comment/$',create_update.create_object, comment_add_info),
#)
#urlpatterns += patterns('KaziKungenxaKabaniNa.Book.views',
#)
#urlpatterns += patterns('',
#    (r'^blog/(?P<object_id>\d+)/$',
#         list_detail.object_detail, blog_detail_info),
#)