# -*-coding:utf-8-*-
# @Time       :2019/12/26 23:41
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :test_div.py
# @Software   :PyCharm
import pytest


def div(a,b):
    return a/b
@pytest.mark.happy
def test_div_int():
    assert div(10,2) == 5
    assert div(10,5) == 2
    assert div(1000000000,1) == 1000000000
    assert div(0,10) == 0
@pytest.mark.happy
def test_div_float():
    assert div(10,3) == 3.3333333333333335
    assert div(10.2,0.2) == 50.99999999999999

@pytest.mark.expection
def test_div_expection():
    assert div('a',10)
    assert div(10,'abc')

@pytest.mark.happy
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        1/0

# >pytest -m "happy"执行标签的用例

#参数化
@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection", {
    (10, 2, 5),
    (10, 5, 2),
    (1000000, 1, 1000000),
    (100,0, 0.5)
})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


