# -*- coding:utf-8 -*-
# @Time    :2020-07-30 10:41
# @Author  :toy_yh
# @File    :base_handle.py
# @Software:PyCharm
import time
import datetime
import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common_handle.handle_log import lg
from common_handle.handle_os import photo_path


class BaseHandle:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele(self, loc, photo_screen, timeout=30, frequency=0.5):
        start_time = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.visibility_of_element_located(locator=loc)
            )
        except:
            lg.exception(msg=f'元素：{photo_screen}_{loc}没有等到')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(f'元素{photo_screen}_{loc}等待显示成功')
            end_time = datetime.datetime.now()
            lg.info(f"等待元素可见开始时间是：{start_time},结束时间是：{end_time},用时是：{end_time-start_time}")

    # 等待元素可点击
    def wait_ele_click_able(self, loc, photo_screen, timeout=30, frequency=0.5):
        start_time = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.element_to_be_clickable(locator=loc)
            )
        except:
            lg.exception(msg=f'元素：{photo_screen}_{loc}不可点击')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'元素：{photo_screen}_{loc}可以点击')
            end_time = datetime.datetime.now()
            lg.info(msg=f'等待元素可点击开始时间：{start_time}, 结束时间：{end_time}, 用时：{end_time-start_time}')

    # 查找元素的封装
    def find_ele(self, loc, photo_screen):
        try:
            ele = self.driver.find_element(*loc)
        except:
            lg.exception(msg=f"查找元素{photo_screen}_{loc}失败")
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'查找元素{photo_screen}_{loc}成功')
            return ele

    # 点击元素的封装
    def click_ele(self, loc, photo_screen):
        self.wait_ele(loc, photo_screen)
        ele = self.find_ele(loc, photo_screen)
        self.wait_ele_click_able(loc,photo_screen)
        try:
            ele.click()
        except:
            lg.exception(msg=f'点击元素{photo_screen}_{loc}失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'点击元素{photo_screen}_{loc}成功')

    # 输入内容的封装
    def input_content(self, loc, photo_screen, content):
        self.wait_ele(loc, photo_screen)
        ele = self.find_ele(loc, photo_screen)
        try:
            ele.send_keys(content)
        except:
            lg.exception(msg=f'元素：{photo_screen}_{loc}中输入内容{content}失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'元素：{photo_screen}_{loc}中输入内容{content}成功')

    # 获取文本封装
    def get_text(self, loc, photo_screen):
        self.wait_ele(loc, photo_screen)
        ele = self.find_ele(loc,photo_screen)
        try:
            result = ele.text
        except:
            lg.exception(msg=f'获取元素{photo_screen}_{loc}的文本内容失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'获取元素{photo_screen}_{loc}的文本内容{result}成功')
            return result

    # 获取属性值
    def get_attribute(self, loc, photo_screen, attr_name):
        self.wait_ele(loc, photo_screen)
        ele = self.find_ele(loc, photo_screen)
        try:
            name = ele.get_attribute(name=attr_name)
        except:
            lg.exception(msg=f'获取元素{photo_screen}_{loc}的属性值失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'获取元素{photo_screen}_{loc}中属性{attr_name}的属性值{name}成功')
            return name

    # 获取所有window的句柄
    def get_all_handles(self, photo_screen):
        try:
            ah = self.get_all_handles()
        except:
            lg.exception('获取所有句柄失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg='获取所有句柄成功')
            return ah

    # 获取最新的句柄（当前句柄）
    def get_new_handle(self, photo_screen):
        ah = self.get_all_handles(photo_screen)
        try:
            now_handle = ah[-1]
        except:
            lg.exception('获取最新句柄失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info('获取当前句柄成功')
            return now_handle

    # 页面滚动至元素显示
    def scroll_loc(self, loc, photo_screen):
        ele = self.find_ele(loc, photo_screen)
        try:
            '''
          element.scrollIntoView()  参数默认为true
          参数为true：调用该函数，页面发送滚动，使element的顶部与视图(容器)顶部对齐
          参数为false：使element的底部与视图(容器)底部对齐  
          '''
            self.driver.execute("arguments[0].scrollIntoView(false);", ele)
        except:
            lg.exception(msg=f'滚动元素{photo_screen}_{loc}失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(f'滚动元素{photo_screen}_{loc}成功')


    # 保存图片
    def _save_photo(self, photo_screen):
        str_time = time.strftime("%Y%d%m%H%M%S", time.localtime(time.time()))
        photo_file = f'{photo_screen}_{str_time}.png'
        screen_photo_path = os.path.join(photo_path, photo_file)
        try:
            self.driver.save_screenshot(filename=screen_photo_path)
        except:
            lg.exception(msg=f'{photo_file}图片保存失败')
            self._save_photo(photo_screen)
            raise
        else:
            lg.info(msg=f'图片{photo_file}保存成功')

