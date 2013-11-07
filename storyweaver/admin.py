from django.contrib import admin
from models import Narrative, Choices, UserProfile, Question, Answer

admin.site.register(Narrative)
admin.site.register(Choices)
admin.site.register(UserProfile)

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
