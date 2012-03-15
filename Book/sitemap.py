from django.contrib.sitemaps import Sitemap
from Book.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "Yearly"
    priority = 0.7
    
    def items(self):
        return Blog.objects.all()
    
    def location(self, obj):
        return '/blog/%s' % obj.title



