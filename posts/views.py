try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

import timeago, datetime

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Post, Image


from django.views.generic import DetailView


def post_list(request):
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)
    home_posts = Post.objects.all().order_by('-timestamp')[:4]
    
    for p in home_posts:
       p.posted_timeago = timeago.format(p.timestamp.replace(tzinfo=None), now)
       p.image_location = Image.objects.filter(post=p)[0].image.url
       if not p.image_location:
           p.image_location = ''


    
    context = {
        'home_posts' : home_posts,
    }
    return render(request, 'index.html', context=context)
    
def post_detail(request, id):
    post = Post.objects.filter(id=id).first()
    images = Image.objects.filter(post=post)
    post.images_locations = []
    for i in images:
        print i.image.url
        post.images_locations.append(i.image.url)
    context = {
        'post' : post,
    }
    return render(request, 'post_details.html', context=context)
	
def post_sub_category_list(request, category):
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)
    posts = Post.objects.filter(Q(category_ar=category) | Q(category_fr=category)).order_by('-timestamp')
    for p in posts:
        p.posted_timeago = timeago.format(p.timestamp.replace(tzinfo=None), now)
        p.image_location = Image.objects.filter(post=p)[0].image.url
        if not p.image_location:
            p.image_location = ''

    context = {
        'category': category,
        'posts': posts,
        
    }
    return render(request, 'posts_sub_category.html', context=context)