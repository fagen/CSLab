from organization.views import DepView, DepHomeView, DepCourseView, DepDescView, DepTeacherView, TeacherDetailView, \
    TeacherListView

from django.urls import path, re_path

# 要写上app的名字
app_name = "organization"

urlpatterns = [
    path('list/', DepView.as_view(), name='dep_list'),
    re_path('home/(?P<dep_id>\\d+)/', DepHomeView.as_view(), name='dep_home'),
    re_path('course/(?P<dep_id>\\d+)/', DepCourseView.as_view(), name="dep_course"),
    re_path('desc/(?P<dep_id>\\d+)/', DepDescView.as_view(), name="dep_desc"),
    re_path('dep_teacher/(?P<dep_id>\\d+)/', DepTeacherView.as_view(), name="dep_teacher"),

    re_path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    re_path('teacher/detail/(?P<teacher_id>\\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),
]
