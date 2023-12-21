import os
# from dataBase import DataBase123123123
import json
from icecream import *

from openpyxl import Workbook, load_workbook

import pandas as pd

    

import os
def findSmaliFolder(decodeFile):
    folderList = []
    for fileName in os.listdir(decodeFile):
        if fileName.find('smali') != -1 :
            folderList.append(os.path.join(decodeFile,fileName))
    return folderList
def highlight_word_in_text(text, word_to_highlight):
    highlighted_text = text.replace(word_to_highlight, '\033[32m{}\033[0m'.format(word_to_highlight))
    return highlighted_text
def isSDKField(decodeAppFolder,pkgName,flag):
    # count = 0
    # 遍历目录内的所有文件和子目录
    for root, dirs, files in os.walk(decodeAppFolder+'/'+pkgName):
        # 遍历当前目录的文件
        for file in files:
            file_path = os.path.join(root, file)
            # 处理文件路径（这里只是打印文件路径作为示例）
            if(flag.lower() in file_path.lower() and 'smali' in file_path.lower()):
                
                text = file_path.lower()
                word_to_highlight = flag.lower()

                # print(highlight_word_in_text(text, word_to_highlight))
                print(pkgName,highlight_word_in_text(text, word_to_highlight))
                # print(pkgName,highlight_word_in_text(file_path))
                return True
                
    return False
    

def main():
    # 解包后的app文件夹
    decodeAppFolder='../data/appDecoded'
    # 索引关键字段
    
    targetFiledList = ["sharesdk"]
    targetFiledList = ["sharesdk",
    # "alipay",
    # "umeng","paypal","facebook"
    ]+[
    # "yandex",
    # "alipay",
    # "AmazonSDK",
    # "Amplitude",
    # "Andriod",
    # "applovin",
    # "AppNext",
    # "appsflyer",
    # "bytedance",
    # "DropBox",
    # "FabricIO",
    # "FBSDK",
    "ad4screen",
    "jiubang",
    # "flurry",
    # "Google",
    # "here",
    # "ironsource",
    # "kakao",
    # "line",
    # "linkin",
    # "MixPanel",
    # "mopub",
    # "onesignal",
    # "paypal",
    # "pinterest",
    # "Pollfish",
    # "Snap",
    # "Square",
    # "startapp",
    # "tapjoy",
    # "tencent",
    # "Twitter",
    # "unity",
    # "VK",
    # "Vungle",
    # "wechat",
    # "ZenDesk",
    # "Zoom,"
    ]
    # 初始化路
    # targetFiledList = []
    # tmp = os.path.join(smaliFile,'com','umeng')
    
    ans=[]
    for i in targetFiledList:
        
        targetFiled = i
        res = {"SDKname":targetFiled}    
        print("\n## sdk name",targetFiled)
        folder_list = os.listdir(decodeAppFolder)
        # print(folder_list)
        
        for pak in folder_list:
            
            # print("### "+pak)
            flag = isSDKField(
                decodeAppFolder
                ,pak
                ,targetFiled)
            if flag:
                res[pak] = flag
            # if(flag):
            #     res["appPath"] = decodeAppFolder+'/'+pak
            #     print(res)
            #     print("### "+res["appPath"])
            # print(flag)
        print(res)
        ans.append(res)
    print(ans)
        



if __name__ == "__main__":
    main()
    
    
    
    