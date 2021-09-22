from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.
# Username admin
# Password liulei123

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
