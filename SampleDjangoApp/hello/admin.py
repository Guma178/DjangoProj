from django.contrib import admin

from .models import Db
from .models import Rubric

# Register your models here.

class DbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_link = ('title', 'content')
    search_field = ('title', 'content')
    
admin.site.register(Db, DbAdmin)
admin.site.register(Rubric)
