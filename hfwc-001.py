# -*-coding:utf-8-*-
# @Time       :2019/12/22 14:10
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :hfwc-001.py
# @Software   :PyCharm

# 元组不可更改，可以用来参数传递
# 集合可以算区别
#词典，关系数据,数据存储，列表可以模拟堆栈和列表
qure=[1,2,3,4]
import pytest
def test_a():
    print("waimiande function")



# import  deque #队列
from collections import deque
que=[1,5.8,3]
que1=deque(que)
que1.append("a")#增加
que1.popleft()#先进先出

def setup_function():
    print("set up function00000000")
def setup_module():
    print("set up module000000")
# def setup_class():
#     print("set up class 0000000")
class Testclass:
    def setup(self):
        print("setupfunction")
    @classmethod
    def setup_class(cls):
        print("setupclass")
    def test_one(self):
        print("test one")
