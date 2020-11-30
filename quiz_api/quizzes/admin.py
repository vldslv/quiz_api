from django.contrib import admin

from .models import Quiz, Question, Attempt, Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'description')
    empty_value_display = 'Не указано'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        return self.readonly_fields


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort_order', 'quiz', 'text', 'answer_type', 'answer')
    list_editable = ('quiz', 'sort_order')
    list_filter = ('quiz',)
    search_fields = ('text',)
    empty_value_display = 'Не указано'


class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'quiz', 'pass_date')
    list_filter = ('user_id',)
    empty_value_display = 'Не указано'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt', 'answer')
    list_filter = ('attempt',)
    empty_value_display = 'Не указано'


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Answer, AnswerAdmin)
