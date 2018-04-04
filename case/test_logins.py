# coding:utf-8
import unittest
import requests
from login import Login
from common.logger import Log

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        s = requests.session()
        self.login = Login(s)

    def test_login(self):
        '''测试登录用例'''
        self.log.info("------start!--------")
        result = self.login.login('huangzhengyang', '123456')
        self.log.info("调用登录结果：{}".format(result))
        name = result['data']['auth']['info']['name']
        self.log.info("获取是用戶名：{}".format(name))
        self.assertEqual(name, 'huangzhengyang')  # 拿结果断言
        self.log.info("------end!--------")

    def test_login_error(self):
        '''测试登录用例'''
        self.log.info("------start!--------")
        result = self.login.login('ohjbrekvbwsj', '1234567')
        self.log.info("调用登录结果：{}".format(result))
        state = result['state']
        self.log.info("获取是用戶名：{}".format(state))
        self.assertEqual(state, 3)  # 拿结果断言
        self.log.info("------end!--------")



if __name__ == "__main__":
   unittest.main()
