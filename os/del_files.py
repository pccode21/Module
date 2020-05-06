"""
本文假设某些特定类型的文件和大小为0的文件为垃圾文件，可以自由扩展代码的列表，也就是垃圾文件的类型。
打开命令提示符窗口ctrl+alt+T，执行命令“python del_files.py c:\test”，其中“c:\test”表示要清理的文件夹，
如果有多个文件夹要清理的话，可以使用空格隔开。
"""
from os.path import isdir, join, splitext
from os import remove, listdir, chmod, stat
import sys

#指定要删除的文件类型
filetypes = ['.tmp', '.log', '.obj', '.txt']

def delCertainFiles(directory):
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            #递归调用
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes or stat(temp).st_size==0:
            #修改文件属性，获取访问权限
            chmod(temp, 0o777)
            #删除文件
            remove(temp)
            print(temp, ' deleted....')

if __name__ == '__main__':
    paths = sys.argv[1:]
    for path in paths:
        if isdir(path):
            delCertainFiles(path)
