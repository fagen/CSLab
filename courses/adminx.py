import xadmin

from .models import Course, Lesson, CourseResource


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    """课程"""
    list_display = ['name', 'desc', 'teacher', 'detail', 'students', 'get_lesson_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'students']
    list_filter = ['name', 'desc', 'detail', 'students']
    model_icon = 'fa fa-book'
    ordering = ['-students']
    readonly_fields = ['students']
    list_editable = ['desc']
    # style_fields = {"detail", "ueditor"}
    # refresh_times = [3, 5]
    inlines = [LessonInline, CourseResourceInline]

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # obj实际是一个course对象
        obj = self.new_obj
        # 如果这里不保存，新增课程，统计的课程数会少一个
        obj.save()
        # 确定课程的课程机构存在。
        if obj.course_dep is not None:
            # 找到添加的课程的课程机构
            course_dep = obj.course_dep
            # 课程机构的课程数量等于添加课程后的数量
            course_dep.course_nums = Course.objects.filter(course_dep=course_dep).count()
            course_dep.save()


class LessonAdmin(object):
    """章节"""
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 这里course__name是根据课程名称过滤
    list_filter = ['course__name', 'name', 'add_time']


# class DocImageAdmin(object):
#     """镜像"""
#
#     list_display = ['lesson', 'name', 'remote_url', 'add_time']
#     search_fields = ['lesson', 'name', 'remote_url']
#     list_filter = ['lesson', 'name', 'remote_url', 'add_time']


class CourseResourceAdmin(object):
    """课程资源"""
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
