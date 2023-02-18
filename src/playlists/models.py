from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from djangoflix.db.models import PublicStateOptions
from djangoflix.db.receiver import pre_save_func, slugify_pre_save
from videos.models import Video

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.all()
    
class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)
    
class Playlist(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices= PublicStateOptions.choices, default=PublicStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False,blank=True, null=True)
    
    objects = PlaylistManager()
    @property
    def is_published(self):
        
        return self.active
pre_save.connect(pre_save_func, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)

    

    