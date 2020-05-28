from django.shortcuts import render
from django.views import generic
from .models import posts

class PostList(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model=posts
    template_name='post_detail.html'
class contact(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='contacts.html'
class home(generic.ListView):
    queryset= posts.objects.order_by('-created_on')
    template_name='home.html'
# Create your views here.
