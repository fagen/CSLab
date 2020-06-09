from datetime import datetime

from django.db import models


# Create your models here.

class CourseDep(models.Model):
    name = models.CharField('部门或学院名称', max_length=50)
    desc = models.TextField('部门描述')
    students = models.IntegerField('学习人数', default=0)
    course_nums = models.IntegerField('课程数', default=0)
    image = models.ImageField('logo', upload_to='dep/%Y%m', max_length=100, default='images/course.jpg')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程部门'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取机构的教师数
        return self.teacher_set.all().count()

    def get_course_nums(self):
        # 获取部门课程数
        return self.course_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    dep = models.ForeignKey(CourseDep, verbose_name='所属部门', on_delete=models.CASCADE)
    name = models.CharField('教师姓名', max_length=50)
    desc = models.TextField('教师简介')
    add_time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(
        default='images/mayun.png',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def get_course_num(self):
        return self.course_set.all().count()

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.dep, self.name)
