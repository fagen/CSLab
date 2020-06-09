from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
from kubernetes.client.rest import ApiException
from pure_pagination import Paginator, PageNotAnInteger

# from courses.kube_connect import create_deployment, create_service
from courses.models import Course, CourseResource
from operation.models import UserCourse, LearningPro
from utils.mixin_utils import LoginRequiredMixin

from kubernetes import client, config
import yaml
import time
config.kube_config.load_kube_config(config_file="D:\\Work_space\\django\\CSLab\\kubeconfig.yaml")
api_instance = client.AppsV1Api()
# for service
CoreV1Api = client.CoreV1Api()

#
# # for service
coreApi = client.CoreV1Api()


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        sort = request.GET.get('sort', "")

        if sort == "students":
            all_courses = all_courses.order_by("-students")

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_courses.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) | Q(
                    detail__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 2, request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            'all_courses': courses,
            'sort': sort,
        })


class CourseDetailView(View):
    """课程详情"""

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, "course-detail.html", {
            'course': course,

        })


class CourseInfoView(LoginRequiredMixin, View):
    """课程章节信息"""

    # 关联课程与学生
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # course.students =
        # 关联学生和课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
            course.students = course.get_learn_user_nums()
            course.save()

        for lesson in course.lesson_set.all():
            learning_pros = LearningPro.objects.filter(user=request.user,
                                                       course=course,
                                                       lesson=lesson,
                                                       )
            # 用户容器添加和保存 container 还没法确定
            if not learning_pros:
                print(request.user)
                learning_pro = LearningPro(user=request.user,
                                           course=course,
                                           lesson=lesson,
                                           )
                learning_pro.save()

        learning_pros = LearningPro.objects.filter(user=request.user,
                                                   course=course
                                                   )

        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "all_resources": all_resources,
            "learning_pros": learning_pros,
        })

#
# class VideoPlayView(LoginRequiredMixin, View):
#     '''课程章节视频播放页面'''
#
#     def get(self, request, learningpro_id):
#         learningpro = LearningPro.objects.get(id=int(learningpro_id))
#         # 通过外键找到章节再找到视频对应的课程
#         course = learningpro.course
#
#         # 查询用户是否已经学习了该课程
#         user_courses = UserCourse.objects.filter(user=request.user, course=course)
#         if not user_courses:
#             # 如果没有学习该门课程就关联起来
#             user_course = UserCourse(user=request.user, course=course)
#             user_course.save()
#
#         course.students = course.get_lesson_nums()
#         course.save()
#         # 相关课程推荐
#         # 找到学习这门课的所有用户
#         # user_courses = UserCourse.objects.filter(course=course)
#         # 找到学习这门课的所有用户的id
#         # user_ids = [user_course.user_id for user_course in user_courses]
#         # 通过所有用户的id,找到所有用户学习过的所有过程
#         # all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
#         # 取出所有课程id
#         # course_ids = [all_user_course.course_id for all_user_course in all_user_courses]
#         # 通过所有课程的id,找到所有的课程，按点击量去五个
#         # relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
#
#         # 资源
#         all_resources = CourseResource.objects.filter(course=course)
#         return render(request, 'course-play.html', {
#             'course': course,
#             'all_resources': all_resources,
#             # 'relate_courses': relate_courses,
#             'learningpro': learningpro,
#         })


class VideoPlayView(LoginRequiredMixin, View):

    def get(self, request, learningpro_id):
        learningpro = LearningPro.objects.get(id=int(learningpro_id))
        if learningpro.valid:
            return redirect(learningpro.container)
        else:
            name = "resource" + str(learningpro.id)
            svc_name = name + "-service"
            dep_name = name + "-deployment"
            namespace = 'default'
            image_url = learningpro.lesson.remote_url
            container_port = 80

            body = {'apiVersion': 'apps/v1',
                    'kind': 'Deployment',
                    'metadata': {'name': dep_name},
                    'spec': {'replicas': 1,
                             'selector': {'matchLabels': {'app': name}},
                             'template': {'metadata': {'labels': {'app': name}},
                                          'spec': {
                                              'containers': [{'name': name,
                                                              'image': image_url,
                                                              # 'env': [{'name': 'VNC_RESOLUTION', 'value': '1400x1050'}],
                                                              'ports': [{'containerPort': 6080}]}]}
                                          }
                             }

                    }
            print("pos2")
            resp = api_instance.create_namespaced_deployment(body=body, namespace="default")
            print(resp)

            time.sleep(3)

            k8s_api_obj = client.CoreV1Api()
            namespace = "default"
            body2 = {'apiVersion': 'v1',
                     'kind': 'Service',
                     'metadata': {'name': svc_name, 'labels': {'app': name}},
                     'spec': {'type': 'NodePort',
                              'ports': [{'port': 6080, 'targetPort': 6080}],
                              'selector': {'app': name}}}
            try:
                api_response = k8s_api_obj.create_namespaced_service(namespace, body2)
                print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

            # res = CoreV1Api.read_namespaced_service(name='test02-service', namespace='default')
            # load_balancer_port = res['spec']['ports'][0]['port']
            # load_balancer_ip = res['status']['load_balancer']['ingress'][0]['ip']
            node_info = CoreV1Api.list_node().items[0]
            # node_name = node_info.metadata.name
            node_ip = node_info.status.addresses[0].address

            svc_info = CoreV1Api.read_namespaced_service(name=svc_name, namespace='default')
            node_port = svc_info.spec.ports[0].node_port
            url = "http://" + node_ip + ":" + str(node_port) + "/"
            learningpro.container = url
            learningpro.valid = True
            learningpro.save()
            return redirect(url)


