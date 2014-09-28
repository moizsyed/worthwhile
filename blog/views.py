from blog.models import Entry, Category
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse

def index(request):
  return render_to_response('index.html', {
    'categories': Category.objects.all(),
    'posts': Entry.objects.all()[:5]
  })

def view_post(request, slug):
  return render_to_response('view_post.html', {
    'post': get_object_or_404(Entry, slug=slug)
  })

def view_category(request, slug):
  category = get_object_or_404(Category, slug=slug)
  return render_to_response('view_category.html', {
    'category': category,
    'posts': Entry.objects.filter(category=category)[:5]
  })