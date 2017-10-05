from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
# Create your models here.
# MVC MODEL VIEW CONTROLLER




class MultilingualModel(models.Model):
    # fallback/default language code
    default_language = None

    # currently selected language
    selected_language = None

    class Meta:
        abstract = True

    def select_language(self, lang):
        """Select a language"""
        self.selected_language = lang
        return self

    def __getattribute__(self, name):
        def get(x):
            return super(MultilingualModel, self).__getattribute__(x)

        try:
            # Try to get the original field, if exists
            value = get(name)
            # If we can select language on the field as well, do it
            if isinstance(value, MultilingualModel):
                value.select_language(get('selected_language'))
            return value
        except AttributeError, e:
            # Try the translated variant, falling back to default if no
            # language has been explicitly selected
            lang = self.selected_language
            if not lang:
                lang = self.default_language
            if not lang:
                raise

            value = get(name + '_' + lang)

            # If the translated variant is empty, fallback to default
            if isinstance(value, basestring) and value == u'':
                value = get(name + '_' + self.default_language)

        return value



class Post(MultilingualModel):
    
    default_language = 'fr'
    
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title_ar = models.CharField(max_length=120)
    title_fr = models.CharField(max_length=120)
    category_ar = models.CharField(max_length=120)
    category_fr = models.CharField(max_length=120)
    
    
    description_ar = models.TextField()
    description_fr = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    posted_timeago = None


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]
        
        
        
class Image(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(Post, default=None)


