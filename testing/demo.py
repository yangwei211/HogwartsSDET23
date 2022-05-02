# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 3:17 下午
@file: demo.py
@desc: 
"""
# 生成器
def provide():
    for i in range(1,10):
        print("start")
        yield i  #yield相当于retuen ,暂停，记住上一次执行位置
        print("end")


provide()

p = provide()
print("第一次")
print(next(p))
print("第二次")
print(next(p))
print("第三次")
print(next(p))