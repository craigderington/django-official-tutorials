from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               { 'fields' : ['question_text']}),
        ('Date information', { 'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)