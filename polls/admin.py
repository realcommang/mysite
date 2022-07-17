from django.contrib import admin
from .models import Question, Choice

# Register your models here.
""" 
choice 객체는 Question 관리자 페이지에서 편집됨. 
기본적으로 3가지 선택 항목 제공.
ChoiceInline(admin.TabularInline): 테이블 기반 형식으로 표시됨.
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

"""
    question text 가 먼저 나오고 그 다음으로 date information이 나온다.
    list_display: question 개별 필드를 표시함. 
    question_text, pub_date, was_published_recently 가 순서대로 표시됨
"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)