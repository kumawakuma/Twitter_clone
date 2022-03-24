from itertools import count
from django import forms
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import postForm
# Create your views here.
def index(request):
    # if the method is POST
    if request.method == 'POST':
     forms = postForm(request.POST, request.FILES)
    # If the form is valid
     if forms.is_valid():
            #yes, save
            forms.save()
          # Redirect to home
            return HttpResponseRedirect('/')
     else:
            # no, Show Error
            return HttpResponseRedirect(forms.erros.as_json())
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    #show
    return render(request, 'posts.html', {'posts': posts})

def delete(request, post_id):
     post = Post.objects.get(id=post_id)
     post.delete()
     return HttpResponseRedirect('/')

def like(request,post_id):
       newlike=Post.objects.get(id=post_id)
       newlike.likecount += 1
       newlike.save()
       return HttpResponseRedirect('/')
    
def edit(request, post_id):
       posts=Post.objects.get(id=post_id)
       if request.method == 'POST':
              forms = postForm(request.POST,request.FILES,instance=posts)
    # If the form is valid
              if forms.is_valid():
            #yes, save
                     forms.save()
          # Redirect to home
                     return HttpResponseRedirect('/')
              else:
            # no, Show Error
                     return HttpResponseRedirect('not valid')
       return render(request, 'edit.html', {'posts': posts})

    