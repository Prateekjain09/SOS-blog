from django.contrib import admin
from .models import(posts)



class postsAdmin(admin.ModelAdmin):
    list_display=('title','created_on','author')

admin.site.register(posts,postsAdmin)
# Register your models here.
