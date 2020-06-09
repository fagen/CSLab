import xadmin
from .models import UserCourse, LearningPro


class UserCourseAdmin(object):
    """用户课程学习"""

    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class LearningProAdmin(object):
    """用户学习进程"""

    list_display = ['user', 'course', 'lesson', 'container', 'update_time', 'valid']
    search_fields = ['user', 'course', 'lesson', 'container']
    list_filter = ['user', 'course', 'lesson', 'container', 'update_time']


xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(LearningPro, LearningProAdmin)

