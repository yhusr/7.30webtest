# -*- coding:utf-8 -*-
# @Time    :2020-07-30 11:29
# @Author  :toy_yh
# @File    :handle_os.py
# @Software:PyCharm

import os


common_path = os.path.dirname(__file__)
root_path = os.path.dirname(common_path)
out_path = os.path.join(root_path, 'out_put')
out_put_path = os.path.join(out_path, 'my_log')


# 保存图片的路径
photo_path = os.path.join(out_path, 'photo_screen')
