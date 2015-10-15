from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',       { 'fields' : ['author', 'title']}),
        ('Article',     { 'fields' : ['blog_text', 'slug']}),
        ('Dates',       { 'fields' : ['pub_date', 'created_date'], 'classes' : ['collapse']}),
        ('Published?',  { 'fields' : ['is_draft']}),
    ]
    list_display = ('title', 'author', 'pub_date', 'created_date', 'is_draft')
    list_filter = ['author', 'pub_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
