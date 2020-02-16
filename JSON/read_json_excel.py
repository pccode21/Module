import json
import os
import pandas as pd

os.chdir(r'.\Module\JSON\data')  # 创建工作路径


def read_json(json_file):
    data = []  # 用于存储每一行的Json数据，列表字典
    with open(json_file, 'r', encoding='UTF-8') as f:  # 将json文件转化为字典
        for line1 in f:
            # read_result = json.loads(line.replace('][', ','))  # 由于原JSON文件的数据是追加写入，需要将‘][]’更换为‘,’
            read_result = json.loads(line1)
            data.append(read_result)
    print(data)
    df = pd.DataFrame()  # 创建基本数据帧是空数据帧
    j = 0
    for line in data:  # 由于data是列表字典[{}, {}]，需要先取出列表中的各个字典
        for i in line:  # 再从字典中取出各项值
            j += 1
            df1 = pd.DataFrame([i], index=[j])  # 在数据帧中自动添加索引
            df = df.append(df1)
    # 在excel表格的第1列写入, 不写入index
    print(df)
    # df.to_excel('json_excel.xlsx', sheet_name='json_data', startcol=0, index=False)  # index=False表示在excel表中不显示索引值
    df.to_csv('json_csv.csv', mode='a', header=False, index=None)  # mode='a'表示可以追加写入


if __name__ == '__main__':
    read_json('search_result.json')
