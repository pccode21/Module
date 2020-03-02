"""标准库itertools模块中有一组用于许多常见数据算法的生成器。例如，groupby可以接受任何序列和一个函数。
它根据函数的返回值对序列中的连续元素进行分组"""
import itertools

first_letter = lambda x: x[0]  # x[0] 表示字符串的第一个字母
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))  # names是一个生成器对象
