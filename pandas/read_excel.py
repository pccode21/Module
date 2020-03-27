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
    print(result, '\n', len(result))
    result = list(dict.fromkeys(result))
    """
    从列表中删除重复项
    使用“列表”项作为键来创建字典。这将自动删除所有重复项，因为字典不能具有重复键
    然后，将字典转换回列表
    """
    print(result, '\n', len(result))
    return index1, result


def list_one_line_to_excel():  # 保存list到本地excel
    index1, result = excel_one_line_to_list()
    df1 = pd.DataFrame(result, columns=index1)
    df1.to_excel('运营商站址名称.xlsx', index=False)

if __name__ == '__main__':
    excel_one_line_to_list()
    list_one_line_to_excel()
