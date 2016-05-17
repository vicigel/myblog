from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
# Create your models here.


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class BlogCategory(models.Model):
#     category_id = models.SmallIntegerField(null=False)
#     category_name = models.CharField(max_length=50,null=False)
#
#
# class BlogInfo(models.Model):
#     category_id = models.ForeignKey(BlogCategory,related_name="category_id")
#     blog_id = models.IntegerField()
#     create_date = models.DateTimeField(default=timezone.now())
#     author = models.CharField(max_length=50)

