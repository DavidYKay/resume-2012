from django.contrib import admin
from models import ExternalSite, Platform, GigType, Gig, Video, Photo, CodeRepo, AppStoreListing

class ExternalSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
admin.site.register(ExternalSite, ExternalSiteAdmin)

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', )
admin.site.register(Platform, PlatformAdmin)

class GigTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'verbose_name', )
admin.site.register(GigType, GigTypeAdmin)

class GigAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('name', 'client', 'tagline', 'end_date')
admin.site.register(Gig, GigAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('gig', 'url', )
admin.site.register(Video, VideoAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo, PhotoAdmin)

class CodeRepoAdmin(admin.ModelAdmin):
    pass
admin.site.register(CodeRepo, CodeRepoAdmin)

class AppStoreListingAdmin(admin.ModelAdmin):
    list_display = ('gig', 'platform',)
admin.site.register(AppStoreListing, AppStoreListingAdmin)
