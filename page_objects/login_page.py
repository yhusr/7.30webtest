# -*- coding:utf-8 -*-
# @Time    :2020-07-30 16:37
# @Author  :toy_yh
# @File    :login_page.py.py
# @Software:PyCharm
from selenium.webdriver.remote.webdriver import WebDriver
from common_handle.base_handle import BaseHandle
from page_loc.login_loc import LoginLoc


class LoginPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def login_operate(self, username, password):
        BaseHandle(self.driver).input_content(loc=LoginLoc.username_loc, photo_screen="登陆页面_用户名输入", content=username)
        BaseHandle(self.driver).input_content(loc=LoginLoc.password_loc, photo_screen='登陆页面_密码输入', content=password)
        BaseHandle(self.driver).click_ele(loc=LoginLoc.login_button_loc, photo_screen='登陆页面_点击登陆按钮')

    def login_wrong_text(self):
        return BaseHandle(self.driver).get_text(loc=LoginLoc.error_login_text_loc, photo_screen='登陆页面_登陆失败的提示')