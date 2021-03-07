from django.contrib import admin
from igapp.models import IGUser, Logined , FBuser
# Register your models here.

class IGUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'ig_username', 'password', 'phone_number', 'fullname']
    list_per_page = 10
admin.site.register(IGUser, IGUserAdmin)

class LoginedAdmin(admin.ModelAdmin):
    list_display = ['id', 'ig_username', 'password']
    list_per_page = 10
admin.site.register(Logined, LoginedAdmin)

class FBUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fb_username', 'password']
    list_per_page = 10
admin.site.register(FBuser, FBUserAdmin)

