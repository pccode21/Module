import pandas as pd
import re
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

os.chdir(r'.\Module\pandas')
all_tools = pd.read_csv('all_tools.csv')


def cleaner(tool_list):
    cleaned_list = ''
    try:
        cleaned_list = []
        for tool in tool_list:
            cleaned_tool = re.findall('^\w+', tool)  # 正则表达式“^\w+”,将工具的名称与字符串的其余部分分开
            # print(cleaned_tool)
            if not cleaned_tool:
                pass
            else:
                cleaned_list.append(cleaned_tool[0])
        cleaned_list = ','.join(cleaned_list)
        return cleaned_list
    except:
        tool_list = ','.join(tool_list)
        'unclean_list'.join(tool_list)
        return tool_list


def give_score(tool_name, offset=0):  # 使用了一个offset变量来添加计数。我们这样做是为了使函数足够灵活，可以添加尚未解析的存储库
    num = all_tools.all_tool_names_cleaned.str.contains(tool_name).sum()  # 使用Pandas的str.contains函数来查找字符串中包含的字段
    num += offset
    print('Count of {} is {} and total usage is {}%'.format(tool_name, num, round((num / (all_tools.shape[0]+offset))*100, 4)))
    # round() 方法返回浮点数x的四舍五入值。

def main():
    print(all_tools.head())  # 查看数据框的前五行
    print(all_tools.shape)  # 打印这个数据帧的形状
    all_tools['all_tool_names_cleaned'] = all_tools.all_tool_names.str.split(',').apply(cleaner)
    print(all_tools)
    give_score('torch')
    print()
    give_score('tensorflow', offset=12)
    """
    对TensorFlow使用了12的偏移量，这是因为有一些实例GitHub存储库没有被解析，
    但是它们来自Google research GitHub用户名或TensorFlow的原始存储库，这清楚地表明它们可能是基于TensorFlow构建的。
    """
    print()
    give_score("keras")
    print(all_tools.all_tool_names_cleaned.str.split(',', expand=True).stack().value_counts()[:50])  # 打印数据中出现频率最高的前50个工具
    all_tools.all_tool_names_cleaned.str.split(',', expand=True).stack().value_counts()[:10].plot(kind='bar')
    plt.show()
    mask = np.array(Image.open("tower.jpg"))
    all_tool_string = ",".join(all_tools.all_tool_names_cleaned)
    wordcloud = WordCloud(background_color=None, mask=mask, mode='RGBA')
    wordcloud.generate(all_tool_string)
    # plt.figure(figsize=(10, 20))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('all_tools.png', dpi=400)
    plt.show()


if __name__ == '__main__':
    main()
