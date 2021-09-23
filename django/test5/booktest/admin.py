from django.contrib import admin
from booktest.models import AreaInfo, PicTest


class AreaInfoStackedInline(admin.StackedInline):
    # model写多类的名字
    model = AreaInfo
    # 额外显示2个可编辑子对象
    extra = 2


class AreaInfoTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2


@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    """地区模型管理类"""
    # 指定每页显示10条数据
    list_per_page = 10
    # 指定要显示的字段
    list_display = ['id', 'title', 'aParent', 'parent']  # 不仅可以写模型类中的属性，也可以写方法
    # 上面的下拉列表框消失
    actions_on_top = False
    # 下拉列表框出现在下面
    actions_on_bottom = True
    # 列表页右侧的过滤栏
    list_filter = ['atitle']
    # 列表也上方的搜索框
    search_fields = ['atitle']

    # 编辑页中显示字段顺序
    # fields = ['aParent', 'atitle']

    # 分组显示
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']}),
    )
    # inlines = [AreaInfoStackedInline]
    inlines = [AreaInfoTabularInline]


# admin.site.register(AreaInfo, AreaInfoAdmin)

admin.site.register(PicTest)
