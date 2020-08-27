from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示""" 
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 外键，建立了与Topic类的多对一的关系
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 没有长度限制 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."

"""笔记
models.Model，Model是Django中定义了模型基本功能的类。
text是由字符串或者文本组成的数据。
date_added是时间戳。
注意：要熟悉可在模型中使用的各种字段，参考：https://docs.djangoproject.com/en/3.1/ref/models/fields/
"""