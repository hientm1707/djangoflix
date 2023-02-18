from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    @property
    def is_published(self):
        return self.active
    # timestamp
    # updated
    # state
    # publish_timestamp
class VideoAllProxy(Video):
    class Meta:
        proxy=True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'
    

class VideoPublishedProxy(Video):
    class Meta:
        proxy=True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'
    

    