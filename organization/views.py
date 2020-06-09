from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage

from courses.models import Course
from organization.models import CourseDep, Teacher
from utils.mixin_utils import LoginRequiredMixin


class DepView(View):
    def get(self, request):
        all_deps = CourseDep.objects.all()
        dep_nums = all_deps.count()
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_deps = all_deps.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))
        # 根据学习人数和课程数排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_deps = all_deps.order_by("-students")
            elif sort == "courses":
                all_deps = all_deps.order_by("-course_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_deps, 2, request=request)
        deps = p.page(page)

        return render(request, 'dep-list.html', {
            "all_deps": deps,
            "dep_nums": dep_nums,
        })


class DepHomeView(View):
    """部门首页"""

    def get(self, request, dep_id):
        # 根据id找到课程机构
        current_page = 'home'
        course_dep = CourseDep.objects.get(id=int(dep_id))
        # 反向查询到课程机构的所有课程和老师
        all_courses = course_dep.course_set.all()[:4]
        all_teacher = course_dep.teacher_set.all()[:2]
        print("部门首页请求到达后台")
        return render(request, 'dep-detail-homepage.html', {
            'course_dep': course_dep,
            'all_courses': all_courses,
            'all_teacher': all_teacher,
            'current_page': current_page,
        })


class DepCourseView(View):
    """
   部门课程列表页
    """

    def get(self, request, dep_id):
        current_page = 'course'
        # 根据id取到课程机构
        course_dep = CourseDep.objects.get(id=int(dep_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_courses = course_dep.course_set.all()
        # 判断收藏状态
        # has_fav = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True

        return render(request, 'dep-detail-course.html', {
            'all_courses': all_courses,
            'course_dep': course_dep,
            'current_page': current_page,
            # 'has_fav': has_fav,
        })


class DepDescView(View):
    '''机构介绍页'''

    def get(self, request, dep_id):
        current_page = 'desc'
        # 根据id取到课程机构
        course_dep = CourseDep.objects.get(id=int(dep_id))
        # 判断收藏状态
        # has_fav = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True
        return render(request, 'dep-detail-desc.html', {
            'course_dep': course_dep,
            'current_page': current_page,
            # 'has_fav': has_fav,
        })


class DepTeacherView(View):
    """
   机构教师页
    """

    def get(self, request, dep_id):
        current_page = 'teacher'
        course_dep = CourseDep.objects.get(id=int(dep_id))
        all_teacher = course_dep.teacher_set.all()
        # 判断收藏状态
        # has_fav = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True

        return render(request, 'dep-detail-teachers.html', {
            'all_teacher': all_teacher,
            'course_dep': course_dep,
            'current_page': current_page,
            # 'has_fav': has_fav,
        })


class TeacherListView(View):
    def get(self, request):
        all_teachers = Teacher.objects.all()
        # 总共有多少老师使用count进行统计
        teacher_nums = all_teachers.count()

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_teachers = all_teachers.filter(name__icontains=search_keywords)
        # 人气排序
        # sort = request.GET.get('sort','')
        # if sort:
        #     if sort == 'hot':
        #         all_teachers = all_teachers.order_by('-click_nums')
        #
        # #讲师排行榜
        # sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]
        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teachers, 1, request=request)
        teachers = p.page(page)
        return render(request, "teachers-list.html", {
            "all_teachers": teachers,
            "teacher_nums": teacher_nums,

        })

class TeacherDetailView(LoginRequiredMixin, View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_course = Course.objects.filter(teacher=teacher)
        # 教师收藏和机构收藏

        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            'all_course': all_course,
        })
