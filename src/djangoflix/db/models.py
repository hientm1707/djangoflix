from django.db import models

class PublicStateOptions(models.TextChoices):
        PUBLISH = 'PU', 'Published'
        DRAFT = 'DR', 'Draft'