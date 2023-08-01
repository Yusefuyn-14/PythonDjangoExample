from django.contrib import admin
from .models import BLog,Referance
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_active","is_home","slug_field")
    list_editable=("is_active","is_home")
    search_fields=("title","description")
    readonly_fields=("slug_field",)

class ReferanceAdmin(admin.ModelAdmin):
    list_display=("name","image")

admin.site.register(BLog,BlogAdmin)
admin.site.register(Referance,ReferanceAdmin)