from datetime import datetime

from django.db import models

# Create your models here.
# from django.db.models import CASCADE
# from DjangoUeditor.models import UEditorField
from organization.models import CourseDep, Teacher


class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    name = models.CharField("课程名", max_length=50)
    desc = models.CharField("课程描述", max_length=300)
    detail = models.TextField("课程详情")
    # detail = UEditorField(verbose_name=u'课程详情', width=600, height=300, imagePath="courses/ueditor/",
    #                       filePath="courses/ueditor/", default='')
    # degree = models.CharField('难度', choices=DEGREE_CHOICES, max_length=2)
    # learn_times = models.IntegerField("学习时长(分钟数)", default=0)
    students = models.IntegerField("学习人数", default=0)
    # fav_nums = models.IntegerField("收藏人数", default=0)
    image = models.ImageField("封面图", upload_to="courses/%Y/%m", max_length=100, default="static/images/course.jpg")
    # click_nums = models.IntegerField("点击数", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now, )
    course_dep = models.ForeignKey(CourseDep, on_delete=models.CASCADE, verbose_name="所属部门", null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True, on_delete=models.CASCADE)
    youneed_know = models.CharField('课程须知', max_length=300, default='')
    teacher_tell = models.CharField('老师告诉你', max_length=300, default='')

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_lesson_nums(self):
        # 获取课程的章节数
        return self.lesson_set.all().count()

    get_lesson_nums.short_description = '章节数'  # 在后台显示的名称

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_learn_user_nums(self):
        return self.usercourse_set.all().count()

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.bit.edu.cn/'>跳转</a>")
    go_to.short_description = "跳转"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField("章节名", max_length=100)
    docImageName = models.CharField("镜像名", max_length=100, default="")
    remote_url = models.CharField('镜像地址', default="", max_length=200)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    # def get_lesson_image(self):
    #     return self.docimage_set.all()

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)


# class DocImage(models.Model):
#     lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
#     name = models.CharField("镜像名", max_length=100)
#     # remote_url = models.CharField("镜像地址", max_length=100)
#     remote_url = models.URLField('镜像地址', default="", max_length=200, null=True, blank=True)
#     local_url = models.CharField("本地镜像路径", max_length=100, null=True, blank=True)
#     add_time = models.DateTimeField("添加时间", default=datetime.now)
#
#     class Meta:
#         verbose_name = "镜像"
#         verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)
    download = models.FileField("资源文件", upload_to="course/resource/%Y/%m", max_length=100)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
