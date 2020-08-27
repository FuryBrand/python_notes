## 步骤

1. 创建project
2. 创建app
3. 修改app/wiews.py
4. 创建app/urls.py
5. 在project/urls.py中配置上面的视图
6. 初始化已有的数据模型(project/settings.py/INSTALLED_APPS)对应的数据库
7. 修改app/models.py以添加数据模型
8. 修改project/settings.py/INSTALLED_APPS以添加APP
9. `py manage.py makemigrations polls` `py manage.py migrate`。使用`py manage.py sqlmigrate polls 0001`可以看到具体要执行什么sql语句
10. 创建admin user。`py manage.py createsuperuser`
11. 将自建的models注册到admin页面
12. 写更多的views
13. 在project/urls.py中配置更多的路径
14. 创建templates文件夹以使用模板


## 测试

```
(fb_env) D:\myExplore\study_notes\study_notes-master (3)\study_notes-master\python_crash_course\django_official_tutorial>python manage.py test polls
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
E
======================================================================
ERROR: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
was_published_recently() returns False for questions whose pub_date
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\myExplore\study_notes\study_notes-master (3)\study_notes-master\python_crash_course\django_official_tutorial\polls\tests.py", line 17, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
  File "D:\myExplore\study_notes\study_notes-master (3)\study_notes-master\python_crash_course\django_official_tutorial\polls\models.py", line 12, in was_published_recently
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
NameError: name 'datetime' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (errors=1)
Destroying test database for alias 'default'...
```


https://docs.djangoproject.com/zh-hans/3.1/intro/tutorial05/