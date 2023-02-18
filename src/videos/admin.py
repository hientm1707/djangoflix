from django.contrib import admin
# Register your models here.
from .models import VideoAllProxy, VideoPublishedProxy, Video

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'active', 'is_published']
    search_fields = ['title']
    ist_filter = ['active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active

admin.site.register(VideoAllProxy, VideoAllAdmin)

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'active', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id', 'is_published']
    def get_queryset(self, request):
        return Video.objects.filter(active=True)
    class Meta:
        model = VideoPublishedProxy
    # def get_queryset(self, request):
    #     return VideoAllProxy.objects.filter(active=True)
    
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
# admin.site.register(VideoAllProxy)
# admin.site.register(VideoPublishedProxy)