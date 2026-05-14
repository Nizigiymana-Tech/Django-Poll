from django.contrib import admin
from .models import Voter, Poll, Question, Choice

# Register your models here.
@admin.register(Voter)
class VoterModel(admin.ModelAdmin):
    fields = ['name', 'age', 'email', 'gender', 'birthdate']
    list_display = ['name', 'age', 'email', 'gender', 'birthdate']
    search_fields = ['name', 'email']
    list_filter = ['gender']


admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)