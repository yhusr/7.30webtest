# -*- coding:utf-8 -*-
# @Time    :2020-07-30 17:38
# @Author  :toy_yh
# @File    :conftest.py.py
# @Software:PyCharm
import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from test_data.common_data import CommonData


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()
    driver.get(CommonData.login_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    yield driver, lp
    driver.quit()


