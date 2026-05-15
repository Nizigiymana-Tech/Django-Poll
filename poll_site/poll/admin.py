from django.contrib import admin
from .models import Respondent, Question, Choice

# Register your models here.
@admin.register(Respondent)
class RespondentsModel(admin.ModelAdmin):
    fields = ['name', 'age', 'email', 'gender', 'birthdate']
    list_display = ['name', 'age', 'email', 'gender', 'birthdate']
    search_fields = ['name', 'email']
    list_filter = ['gender']


admin.site.register(Question)
admin.site.register(Choice)