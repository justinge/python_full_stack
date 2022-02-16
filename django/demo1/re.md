django-admin startproject demo1

setting  项目的配置文件
urls  URL的配置文件
manage 管理文件
wsgi   web服务器的入口
创建应用
python manage.py startapp booktest
设计模型

python manage.py makemigrations  生成迁移文件
执行迁移
python manage.py migrate

django 的后台管理
#python 3.7   django 1.8.2 产生一些不兼容
conda create --name Django_Demo python=3.6
activate Django_Demo
#视图和Url
http://127.0.0.1:8000/admin/  浏览器就给我们显示了后台登录页面 
对这个请求 进行处理动作帮我们产生页面返回回来 视图完成的
MVT    URl请求是视图  视图接收请求后进行处理  --处理结果给请求者
自定义视图
1.定义视图函数
2.配置URLconf

用模板分三步走
1.找到模板
2.定义上线文
3.渲染模板