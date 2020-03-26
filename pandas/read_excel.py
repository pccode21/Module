import pandas as pd
import os

os.chdir(r'.\Module\pandas')

def excel_one_line_to_list():  # 读取excel一列或者多列保存为列表
    df1 = pd.read_excel('塔类产品服务费结算详单-揭阳市-202002.xlsx', sheet_name='202002塔类详单2096', usecols=[6], names=None)
    df1_list = df1.values.tolist()
    index1 = list(df1.keys())
    print(index1)
    result = []
    for list1 in df1_list:
        result.append(list1[0])
    del result[-3:]  # 删除列表最后的3个 nan
    # 以下是去掉列表中重复的字符串的操作
    last = result[-1]  # 取出列表中的最后一个数
    for i in range(len(result)-2, -1, -1):
    # 在这里，len(List)-2是指列表中的倒数第二个数，-1是指列表中的第一个数，步长是-1表示列表从后往前扫描
    # range(start, stop[, step])
    # start: 计数从 start 开始。默认是从 0 开始。
    # stop: 计数到 stop 结束，但不包括 stop
    # step：步长，默认为1
        if last == result[i]:
            del result[i]
            # print(result[i])
        else:
            last = result[i]
    print(result, '\n', len(result))
    return index1, result


def list_one_line_to_excel():  # 保存list到本地excel
    index1, result = excel_one_line_to_list()
    df1 = pd.DataFrame(result, columns=index1)
    df1.to_excel('运营商站址名称.xlsx', index=False)

if __name__ == '__main__':
    excel_one_line_to_list()
    list_one_line_to_excel()
