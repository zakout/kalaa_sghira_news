from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


from posts.models import Post



def index(request):
    return redirect('%s?next=%s' % ('/posts', '/posts/sports'))
