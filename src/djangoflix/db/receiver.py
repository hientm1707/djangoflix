from django.utils import timezone
from django.utils.text import slugify

from . models import PublicVideoStateOptions


def pre_save_func(sender, instance, *args, **kwargs):
        is_publish = instance.state == VideoStateOptions.PUBLISH and instance.published_timestamp is None
        is_draft = instance.state == instance.VideoStateOptions.DRAFT
        if is_publish:
            instance.published_timestamp = timezone.now()
            print('Saved as timstamppublished')
        elif is_draft:
            instance.published_timestamp = None

def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)
