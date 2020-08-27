from django.contrib import admin
from learning_logs.models import Topic, Entry
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

"""学习笔记
1. 导入我们要注册的模型——Topic
2. 让Django通过管理网站管理我们的模型
"""