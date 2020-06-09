from django.urls import path, include, re_path

from users.views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView

app_name = 'users'
urlpatterns = [
    # 用户信息
    path("info/", UserinfoView.as_view(), name='user_info'),
    path("image/upload/", UploadImageView.as_view(), name='image_upload'),
    path("update/pwd/", UpdatePwdView.as_view(), name='update_pwd'),
    path("sendemail_code/", SendEmailCodeView.as_view(), name='sendemail_code'),
    path("update_email/", UpdateEmailView.as_view(),name='update_email'),
    path("mycourse/", MyCourseView.as_view(), name='mycourse'),
]
