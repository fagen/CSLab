import xadmin
from xadmin import views
from .models import EmailVerifyRecord


# 不是很懂
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
#
class GlobalSettings(object):
    # 修改title
    site_title = 'CSLab后台管理界面'
    # 修改footer
    site_footer = '666的公司'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
