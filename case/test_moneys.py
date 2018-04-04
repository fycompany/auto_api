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
        self.s = requests.session()
        self.login = Login(self.s)
        self.url = '/'.join([self.login.base_url, 'records/money'])
        self.token = self.login.get_token()
        self.header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Authorization": self.token
        }


    def test_money(self):
        '''测试存提记录'''
        self.log.info("------start!--------")
        res = self.s.get(self.url, headers=self.header, verify=False)
        r = res.json()
        self.log.info("调用存提记录结果：{}".format(r))
        state = r['state']
        self.log.info("获取是请求状态：{}".format(state))
        self.assertEqual(state, 0)  # 拿结果断言
        self.log.info("------end!--------")



if __name__ == "__main__":
   unittest.main()
