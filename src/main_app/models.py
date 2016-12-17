from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.timezone import activate
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    item_type = 'note'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_note_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = create_slug(instance)
        
pre_save.connect(pre_save_note_receiver, sender=Note)

class Project(models.Model):
    user = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    document = models.FileField(upload_to='project_files', verbose_name='document')
    item_type = 'project'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug})
        
def pre_save_project_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = create_slug(instance)
        
pre_save.connect(pre_save_project_receiver, sender=Project)

class Comment(models.Model):
    note = models.ForeignKey('Note', related_name="comments")
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.comment