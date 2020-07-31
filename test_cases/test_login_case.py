# -*- coding:utf-8 -*-
# @Time    :2020-07-30 17:32
# @Author  :toy_yh
# @File    :test_login_case.py.py
# @Software:PyCharm
import pytest
import time
from test_data.common_data import CommonData
from test_data.login_case_data import LoginCaseData


@pytest.mark.master
@pytest.mark.usefixtures('set_up')
class TestLogin:

    @pytest.mark.parametrize('right_data', LoginCaseData.right_data)
    def test_login_0_right(self, set_up, right_data):
        set_up[1].login_operate(username=right_data['username'], password=right_data['password'])
        time.sleep(2)
        assert set_up[0].current_url == CommonData.index_url

    @pytest.mark.parametrize('wrong_data', LoginCaseData.error_data)
    def test_login_1_wrong(self, set_up, wrong_data):
        set_up[1].login_operate(username=wrong_data['username'], password=wrong_data['password'])
        assert set_up[1].login_wrong_text() == wrong_data['value']
