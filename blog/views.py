from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import BlogPost
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import BlogPostForm


def index(request):
    return render(
        request, 'index.html')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-publication_date']  


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('index')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('index')