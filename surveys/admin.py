from django.contrib import admin
from .models import Survey, Question, CustomUser, Answer


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'description', 'active']
    fields = ['name', 'start_date', 'end_date', 'description', 'active']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'answer_type', 'survey']
    fields = ['name', 'answer_type', 'survey']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CustomUser)
admin.site.register(Answer)
