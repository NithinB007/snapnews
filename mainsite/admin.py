from django.contrib import admin

from .models import SiteSettings, HomePageSettings, SocialSetting,Contact


admin.site.register(SiteSettings)
admin.site.register(HomePageSettings)
admin.site.register(SocialSetting)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'submitted_at')



