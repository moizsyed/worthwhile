from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worthwhilesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(
        r'^blog/post/(?P<slug>[^\.]+)',
        'blog.views.view_post',
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)',
        'blog.views.view_category',
        name='view_blog_category'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# TAKE STATIC LINE OUT BEFORE PRODUCTION!