import xadmin
from xadmin import views
from .models import Menu,Orders,OrdersMain,Shop,Address,Disk,Evaluate
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True

class GlobalSettings(object):
    # 修改title
    site_title = '外卖后台管理界面'
    # 修改footer
    site_footer = '外卖公司'
    # 收起菜单
    menu_style = 'accordion'
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
class MenuAdmin(object):
    list_display = ['title', 'parentId', 'isParentid']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['title', 'parentId', 'isParentid']
    # 过滤
    list_filter = ['title', 'parentId', 'isParentid']
class OrdersAdmin(object):

    list_display = ['orderid', 'totalMoney', 'remarks', 'addressid', 'diskid', 'status', 'isEvaluate','num']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['orderid', 'totalMoney', 'remarks', 'addressid', 'diskid', 'status', 'isEvaluate','num']
    # 过滤
    list_filter = ['orderid', 'totalMoney', 'remarks', 'addressid', 'diskid', 'status', 'isEvaluate','num']

class OrdersMainAdmin(object):
    list_display = ['orderid', 'totalMoney', 'remarks', 'status', 'isEvaluate','createtime']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['orderid', 'totalMoney', 'remarks', 'status', 'isEvaluate','createtime']
    # 过滤
    list_filter = ['orderid', 'totalMoney', 'remarks', 'status', 'isEvaluate','createtime']
class ShopAdmin(object):
    list_display = ['name', 'address', 'time','phone']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['name', 'address', 'time','phone']
    # 过滤
    list_filter = ['name', 'address', 'time','phone']
class AddressAdmin(object):
    list_display = ['openid', 'name', 'mobile','gender','address','isDefault']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['openid', 'name', 'mobile','gender','address','isDefault']
    # 过滤
    list_filter = ['openid', 'name', 'mobile','gender','address','isDefault']
class DiskAdmin(object):
    list_display = ['menuId', 'img', 'title','price','disPrice','sellPoint','created','updated','sellnum','status']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['menuId', 'img', 'title','price','disPrice','sellPoint','created','updated','sellnum','status']
    # 过滤
    list_filter = ['menuId', 'img', 'title','price','disPrice','sellPoint','created','updated','sellnum','status']
class EvaluateAdmin(object):
    list_display = ['diskid', 'orderid', 'openid','imgs','content','evalValue','created','isAnonymous','nickname','avatarUrl']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['diskid', 'orderid', 'openid','imgs','content','evalValue','created','isAnonymous','nickname','avatarUrl']
    # 过滤
    list_filter = ['diskid', 'orderid', 'openid','imgs','content','evalValue','created','isAnonymous','nickname','avatarUrl']
xadmin.site.register(Menu,MenuAdmin)
xadmin.site.register(Orders,OrdersAdmin)
xadmin.site.register(OrdersMain,OrdersMainAdmin)
xadmin.site.register(Shop,ShopAdmin)
xadmin.site.register(Address,AddressAdmin)
xadmin.site.register(Disk,DiskAdmin)
xadmin.site.register(Evaluate,EvaluateAdmin)
