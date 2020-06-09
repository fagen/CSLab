import xadmin

from .models import CourseDep, Teacher


class CourseDepAdmin(object):
    """部门"""

    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class TeacherAdmin(object):
    """老师"""

    list_display = ['name', 'dep', 'desc', 'add_time']
    search_fields = ['name', 'dep', 'desc']
    list_filter = ['name', 'dep', 'desc', 'add_time']


xadmin.site.register(CourseDep, CourseDepAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
