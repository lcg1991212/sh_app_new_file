import allure
import pytest


class Test_001:

    @allure.step(title="测试步骤1")
    def test_001(self):
        allure.attach("描述","我是测试步骤1的描述")
        print("--->test_001")
        assert True
