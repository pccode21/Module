import os
import random
import ctypes
import time

class Change(object):
    def file_name(self,file_dir):#获取指定目录下的所有jpg、gif格式的壁纸
        filePathList = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == ".gif":
                    filePathList.append(os.path.join(root, file))
        return filePathList

    def main(self):
        filePathList = self.file_name(r"D:\GitHub\风景")#修改这里即可使用
        while True:
            filePath = random.choice(filePathList) #随机选择一张图片
            ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0) #设为壁纸
            time.sleep(60) #间隔更换壁纸时间


if __name__ == "__main__":
    Change().main()
