from django.contrib import admin
from .models import Question, Choice
# Register your models here

class QuetionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': [ 'question_text']}),
        ('Date informaition' , {'fields':['pub_date'], 'classes':
                                ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuetionAdmin)