from django.contrib import admin
from models import Article
# Register your models here.

class articleAdmin(admin.ModelAdmin):
    list_display = ['title','block','ower','status','create_timestmp','last_timestmp']
    search_fields = ['title','content']
    list_filter = ['block']

admin.site.register(Article, articleAdmin)
