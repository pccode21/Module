# -*- coding: UTF-8 -*-
'''
@Author ：Jason
@Desc   ：http://www.bizhi360.com/
360壁纸采集
网站壁纸一共15个类
'''
import requests
from lxml import etree
import os
import re
import time

def getImageTypeAndName():
    '''
    主要抓取壁纸分类链接 和 壁纸分类名称
    :返回壁纸分类连接 壁纸分类名称
    '''
    url = "http://www.bizhi360.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    }
    res = requests.get(url=url,headers = headers)
    res.encoding = "gbk"
    etreeHtml = etree.HTML(res.text)
    imageType = etreeHtml.xpath('//div[@id="tagnav"]//div[@class="container"]/a/@href')
    imageTypeName = etreeHtml.xpath('//div[@id="tagnav"]//div[@class="container"]/a/text()')

    return imageType[1:],imageTypeName[1:] #去掉/desk/ 和 壁纸图片大全 这一分类，包含所有图片

def downloadImage():
    '''
    直接采集图片，根据图片分类保存到指定文件夹
    :return:None
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    }
    sourceUrl1 = "http://www.bizhi360.com"
    sourceUrl2 = "http://pic.bizhi360.com/bbpic/"

    imageType, imageTypeName  = getImageTypeAndName()
    for i,url in enumerate(imageType):
        if os.path.exists(imageTypeName[i]): #文件夹存在，不操作
            pass
        else:#文件夹不存在，创建文件夹
            os.mkdir(imageTypeName[i])
            print("创建文件夹")
        for page in range(1,1000): #先假设每个分类有1000页，后期增加判断条件可提前结束
            listUrl = sourceUrl1 + url  + "list_" + str(page) + ".html"
            print(listUrl)
            res = requests.get(listUrl, headers = headers)
            res.encoding = "gbk"

            etreeHtml = etree.HTML(res.text)
            imageUrlList = etreeHtml.xpath('//*[@id="main"]/div/div[1]/ul/li/a/img/@src')
            for imageUrl in imageUrlList:
                url1 = re.findall(r'/(\d+).*?\.jpg',imageUrl)
                realImgUrl = sourceUrl2 + url1[0][-2:] + "/" +url1[0] + ".jpg"
                print(realImgUrl)
                resImg = requests.get(url=realImgUrl,headers=headers)
                with open("./"+imageTypeName[i] +"/"+ url1[0] + ".jpg","wb") as f:
                    f.write(resImg.content)
                    print("壁纸", url1[0] + ".jpg","保存完毕")
            if "<span>下一页</span>" in res.text:#判断抓取终止条件，存在那么就停止抓取
                break

if __name__ == "__main__":
    # getImageTypeAndName()
    downloadImage()
    print("  ")
