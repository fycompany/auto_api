# coding:utf-8
import requests

from common.logger import Log
from config import readConfig
# 禁用安全请求警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Login:
    # s = requests.session()  # 全局参数
    log = Log()
    def __init__(self, s):
        self.s = s
        self.base_url = readConfig.base_url

    def login(self, username, password):
        url = "/".join([self.base_url, 'user/login'])
        header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        json_data = {
            "name": username,
            "password": password,
        }


        res = self.s.post(url, headers=header, json=json_data, verify=False)
        r = res.json()  # 字节输出
        self.log.info("调用登录方法，获取结果：{}".format(r))
        return res.json()

    def get_token(self):
        # 提取token
        r = self.login('huangzhengyang', '123456')
        token = r['data']['auth']['token']
        self.log.info("token，获取结果：{}".format(token))
        return token

    def logout(self):
        url = "/".join([self.base_url, 'user/logout'])
        res = self.s.get(url, verify=False)
        self.log.info("调用退出方法：{}".format(res.json()))


if __name__ == "__main__":
    import requests
    s = requests.session()
    Login(s).get_token()