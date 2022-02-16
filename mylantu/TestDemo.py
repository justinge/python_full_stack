import unittest
from  maildemo import app

class TestCase(unittest.TestCase):
    #启动测试环境
    def setUp(self):
        self.app=app
        app.config['TESTING']=True
        self.client=self.app.test_client()

    def test_email(self):
        resp=self.client.get('/')
        print(resp.data)
