from django.db import models
from django.db.models import permalink

class Entry(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  created = models.DateTimeField(db_index=True, auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  category = models.ForeignKey('blog.Category')
  source = models.ForeignKey('blog.Source', null=True)

  def __unicode__(self):
    return '%s' % self.title

  class Meta:
    verbose_name = "Blog Entry"
    verbose_name_plural = "Blog Entries"
    ordering = ["-created"]

  @permalink
  def get_absolute_url(self):
    return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
  title = models.CharField(max_length=100, db_index=True)
  slug = models.SlugField(max_length=100, db_index=True)

  def __unicode__(self):
    return '%s' % self.title

  @permalink
  def get_absolute_url(self):
    return ('view_blog_category', None, { 'slug': self.slug })


class Source(models.Model):
  name = models.CharField(max_length=200, db_index=True, blank=True, default="")
  link = models.URLField(max_length=300, blank=True, default="")

  def __unicode__(self):
    return '%s' % self.name

