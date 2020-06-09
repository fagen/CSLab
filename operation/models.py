from datetime import datetime

from django.db import models

# Create your models here.
from users.models import UserProfile
from courses.models import Course, Lesson


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


class LearningPro(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    container = models.CharField('容器id', max_length=100, default='', null=True, blank=True)
    valid = models.BooleanField('容器链接是否有效', default=False)
    url = models.URLField('远程桌面链接', default='', max_length=200, null=True, blank=True )
    update_time = models.DateTimeField('修改时间', default=datetime.now)

    class Meta:
        verbose_name = '章节进程'
        verbose_name_plural = verbose_name





