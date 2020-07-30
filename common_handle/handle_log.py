# -*- coding:utf-8 -*-
# @Time    :2020-07-30 11:05
# @Author  :toy_yh
# @File    :handle_log.py
# @Software:PyCharm
import time
import logging
import os
from common_handle.handle_os import out_put_path


class Logger:

    @classmethod
    def get_logger(cls):
        logger = logging.getLogger("web_test")
        log_formate = logging.Formatter(fmt='%(asctime)s - %(name)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        logger.setLevel("DEBUG")

        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        sh.setFormatter(log_formate)
        logger.addHandler(sh)

        # 文件输出日志
        stf_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_path = os.path.join(out_put_path, stf_time + 'log.log')
        fh = logging.FileHandler(filename=log_path, mode='w', encoding='utf8')
        fh.setFormatter(log_formate)
        fh.setLevel("DEBUG")
        logger.addHandler(fh)

        return logger


lg = Logger.get_logger()