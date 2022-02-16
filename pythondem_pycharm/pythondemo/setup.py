from distutils.core import setup
setup(name="pa_message",#包名,
      version="1.0",#版本
      description="发送消息模块",
      long_description="完整的发送接收模块",
      author="song",
      author_email="112@qq.com",
      url="www.baidu.com",
      py_modules=[
          "pa_message.send_message",
          "pa_message.re_message"

      ])