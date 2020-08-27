很不幸的是，该书在视图阶段和目前的Django3.1 差异逐渐变大。我决定使用官方提供新手文档继续。反正后面做工具的话，前端应该要选用VUE吧，Django提供Http服务

## 建立虚拟环境

首先尝试使用该命令：`lesson04_learning_log> python -m venv ll_env`

如果上述命令报错，则可能需要安装virtualenv包。使用如下命令：
- 方式1：`pip install --user virtualenv`
- 方式2：`sudo apt-get install python-virtualenv`

安装好之后使用该命令创建虚拟环境：`virtualenv ll_env` 。若需要指定python版本则使用参数如：`virtualenv ll_env ——python=python3`

## 激活虚拟环境

Linux首先尝试使用该命令：`source ll_env/bin/activate`
Windows使用cmd：`ll_env\Scripts\activate`

## 停止使用虚拟环境

命令：`deactivate`

## 在虚拟环境中安装Django

命令：`pip install Django`

## 在Django中创建项目

命令：`django-admin startproject learning_log .`

#### Django项目目录结构介绍

- `manage.py`接受命令并交给Django的相关部分去执行。
- `learning_log/settings.py`指定Django如何与系统交互以及如何管理项目。
- `learning_log/urls.py`告诉Django应创建哪些网页来响应浏览器请求。
- `learning_log/wsgi.py`帮助Django提供它创建的文件，这是Web Server Gateway Interface的缩写。

## 创建数据库

命令：`python manage.py migrate`

## 查看项目

命令：`python manage.py runserver`

## 创建应用

命令：`python manage.py startapp learning_logs`

#### Django应用目录结构介绍

- `learning_logs/models.py`定义应用程序中管理的数据。
- `learning_logs/admin.py`向Django管理端注册要管理哪些数据。

## 创建自建应用模型的数据库

```cmd 
lesson04_learning_log>python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs\migrations\0001_initial.py
    - Create model Topic
lesson04_learning_log>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```

- 首先使用makemigrations让Django确定该如何修改数据库来存储以新定义的模型来保存的数据，并生成名为0001_initial.py的迁移文件。
- 随后使用migrate来使迁移生效。

修改程序管理的数据时，需要三步：
1. 修改models.py
2. 使用makemigrations
3. 使用migrate

## Django的admin site

创建超级用户：`python manage.py createsuperuser`
- root
- furybrand@outlook.com
- root2020

## 使用Django Shell

Django Shell是测试项目和排除故障的理想之地。`python manage.py shell`
```
lesson04_learning_log>python manage.py shell
Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()                            
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>> topics = Topic.objects.all()
>>> for topic in topics:   
...     print(topic.id, topic) 
... 
1 Chess
2 Rock Climbing
>>> t = Topic.objects.get(id = 1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2020, 8, 27, 3, 19, 47, 445443, tzinfo=<UTC>)
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry: In the opening phase of the game, it's important t...>]>
>>>
```

## 创建网页

1. 定义URL
2. 编写试图
3. 编写模板