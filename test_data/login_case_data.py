# -*- coding:utf-8 -*-
# @Time    :2020-07-30 17:30
# @Author  :toy_yh
# @File    :login_case_data.py.py
# @Software:PyCharm


class LoginCaseData:
    # 正向登录用例的数据
    right_data = [{'username': '18612132018', 'password': 'python'},
                  {'username': ' 18612132018', 'password': 'python'}]

    # 反向登录用例的数据
    error_data = [{'username': '', 'password': 'python', 'value': '账号登录'},
                  {'username': '18684720553', 'password': '', 'value': '账号登录'},
                  {'username': '', 'password': '', 'value': '账号登录'}]