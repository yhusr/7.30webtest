# -*- coding:utf-8 -*-
# @Time    :2020-07-30 17:38
# @Author  :toy_yh
# @File    :contest.py.py
# @Software:PyCharm
import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()


