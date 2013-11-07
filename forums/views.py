from forums.models import Category, Thread, Post, Document
from django.views import generic
from django import forms
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
# Create your views here.

class CategoryList(generic.ListView):
    model = Category

class ThreadList(generic.ListView):
    model = Thread

    def get_queryset(self):
        return Thread.objects.filter(category=self.kwargs['pk'])
        
class PostList(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(thread=self.kwargs['pk'])

class DocumentList(generic.ListView):
    model = Document

class PostForm(forms.ModelForm):
    class Meta:
      model = Post
      exclude = ("poster", "thread")

class PostCreation(generic.CreateView):
    form_class = PostForm
    thread = ''

    def get_context_data(self, **kwargs):
        context = super(PostCreation, self).get_context_data(**kwargs)
        context["thread"] = get_object_or_404(Thread, pk=self.request.META['HTTP_REFERER'].split('/')[5])
        PostCreation.thread = context["thread"]
        return context

    def form_valid(self, form):
        object = form.save(commit=False)
        object.poster = self.request.user
        object.thread = self.thread
        object.save()
        return HttpResponseRedirect("/forums/thread/" + str(object.thread.id))

class DocumentForm(forms.ModelForm):
    class Meta:
      model = Document
      exclude = ("poster")

class DocumentSubmission(generic.CreateView):
    form_class = DocumentForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.poster = self.request.user
        object.save()
        return HttpResponseRedirect("/forums/documents/")
