import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
"""
question_text : char형 (최대길이 200)
dateTimeFiel : 날짜와 시간 표현
__str__ : question_text가 편하게 보이도록 설정
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

""" 
foreinkey : choice가 한 question에 관계됨
choice_text : char형, max_length:200
"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text