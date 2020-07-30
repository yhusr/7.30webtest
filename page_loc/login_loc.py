# -*- coding:utf-8 -*-
# @Time    :2020-07-30 17:00
# @Author  :toy_yh
# @File    :login_loc.py.py
# @Software:PyCharm
from selenium.webdriver.common.by import By


class LoginLoc:
    # 登录页面用户名的定位
    username_loc = (By.NAME, 'account')
    # 登录页面密码的定位
    password_loc = (By.NAME, 'pass')
    # 登录页面登录按钮的定位
    login_button_loc = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
    # 登录失败的错误文本显示
    error_login_text_loc = (By.XPATH, '//a[@class="active"]')
