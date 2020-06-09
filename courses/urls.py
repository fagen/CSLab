# course/urls.py

from django.urls import path, re_path
from .views import CourseListView, CourseDetailView, CourseInfoView, VideoPlayView

# 要写上app的名字
app_name = "course"

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    re_path('detail/(?P<course_id>\\d+)/', CourseDetailView.as_view(), name="course_detail"),
    re_path('info/(?P<course_id>\\d+)/', CourseInfoView.as_view(), name="course_info"),
    re_path('video/(?P<learningpro_id>\\d+)', VideoPlayView.as_view(), name='video_play'),
]