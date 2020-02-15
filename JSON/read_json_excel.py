import json
import os
import pandas as pd

os.chdir(r'.\Module\JSON\data')  # 创建工作路径


def read_json(json_file):
    data = []  # 用于存储每一行的Json数据
    with open(json_file, 'r', encoding='UTF-8') as f:  # 将json文件转化为字典
        for line in f:
            read_result = json.loads(line.replace('][', ','))
            data.append(read_result)
    df = pd.DataFrame()  # 最后转换得到的结果
    for line in data:
        for i in line:
            df1 = pd.DataFrame([i])
            df = df.append(df1)
    # 在excel表格的第1列写入, 不写入index
    df.to_excel('json_excel.xlsx', sheet_name='json_data', startcol=0, index=False)


if __name__ == '__main__':
    read_json('search_result.json')
