from django.contrib import admin
from django.utils import timezone
import datetime

from .models import Choice, Question


#class ChoiceInline(admin.StackedInline):  atack look, It takes more space at admin page.
#   model = Choice
#  extra = 3

class ChoiceInline(admin.TabularInline):    #Tabular look at admin page
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question statement',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    
admin.site.register(Question,QuestionAdmin)