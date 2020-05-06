"""
Python标准库os模块的walk函数提供了遍历一个文件夹的功能，它返回一个生成器。
"""
import os

g = os.walk('E:/2019年-运行维护部/My-job/无线室')
for path, dir_list, file_list in g:
    for dir_name in dir_list:
        print(os.path.join(path, dir_name))
    for file_name in file_list:
        print(os.path.join(path, file_name))
