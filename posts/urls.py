from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_sub_category_list,
	post_detail,
	)

urlpatterns = [
	url(r'^(?P<category>\w+)/$', post_sub_category_list, name='sub_category_list'),
	url(r'^detail/(?P<id>\d+)/$', post_detail, name='detail'),
	url(r'^$', post_list, name='list'),
]