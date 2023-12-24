
# 仅仅检查是否存在类似
# com.picooc.international\smali_classes4\com\umeng\analytics 
# 路径

import itertools
import os
# from dataBase import DataBase123123123
import json
from icecream import *
# from DataBase import DataBase
from openpyxl import Workbook, load_workbook

import pandas as pd

# DECODE_FOLDER='./appDecoded'
DECODE_FOLDER = os.path.abspath('../data/appDecoded')

print(DECODE_FOLDER)


def findSmaliFolder(Appdir):
    folderList = []
    for fileName in os.listdir(Appdir):
        if fileName.find('smali') != -1 :
            folderList.append(os.path.join(Appdir,fileName))
    return folderList

def InsertMaindianInfo():    
    totList ={"apps":[]}
    
    Result = {"Umeng":set(),
            "sharesdk":set(),
            "Firebase":set(),
            'yandex':set(),
            "GA":set(),
            "ad4screen":set(),
            "jiubang":set(),
            "Kissmetrics":set(),
            "Mixpanel":set(),
            "Heap":set(),
            "GrowingIO":set(),
            "Sensors":set(),
            "Baidu":set(),
            "Talkingdata":set(),
            "Zhuge":set(),
            "Amplitude":set()}
    # growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
    # Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
            # "Kissmetrics":set(),
            # "Mixpanel":set(),
            # "Heap":set(),
            # "GrowingIO":set(),
            # "Sensors":set(),
            # "Baidu":set(),
            # "Talkingdata":set(),
            # "Zhuge":set(),
            # "Amplitude":set()}
    for appName in os.listdir(DECODE_FOLDER):
        Umeng = GA = Firebase = sharesdk = yandex =jiubang=ad4screen=0
        
        growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
        Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
        
        
        # example output: "appDecoded\com.q1.knifesling"
        Appdir =  os.path.join(DECODE_FOLDER,appName)
        samliFiles = findSmaliFolder(Appdir)
        # growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
        # Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
        print()
        print(appName)
        
        # res = {SDKname:[applist]} 结果使用 sdk->app list的形式输出
        
        # growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
        # Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
        
        for smaliFile in samliFiles:
            # 检查是否存在 "appDecoded\com.q1.knifesling\com"
            if not os.path.exists(os.path.join(smaliFile,'com')):
                continue
            else :
                
                
                # com.umeng.socialize.txt
                # 检查是否存在 "appDecoded\com.q1.knifesling\com\umeng\xxxxxx"
                if os.path.exists(os.path.join(smaliFile,'com','umeng','socialize')) :
                    # print(os.path.join(smaliFile,'com','umeng','analytics'))
                    print(' --Umeng socialize')  
                    
                    Result['Umeng'].add(appName)
                    Umeng = 1
                    
                if os.path.exists(os.path.join(smaliFile,'com','umeng','analytics')) :
                    # print(os.path.join(smaliFile,'com','umeng','analytics'))
                    print(' --Umeng analytics') 
                    Result['Umeng'].add(appName)
                    Umeng = 1
                
                # sharesdk
                if os.path.exists(os.path.join(smaliFile,'cn','sharesdk')) :
                    # print(os.path.join(smaliFile,"cn","sharesdk"))
                    print(' --sharesdk')  
                    Result['sharesdk'].add(appName)
                    sharesdk = 1
                    
                
                # GA
                if os.path.exists(os.path.join(smaliFile,'com','google','android','gms','analytics')) :
                    # print(os.path.join(smaliFile,'com','google','android','gms','analytics'))
                    print(' --GA')  
                    Result['GA'].add(appName)
                    GA=1
                    
                # Firebase
                if os.path.exists(os.path.join(smaliFile,'com','google','firebase')) :
                    print(' --Firebase') 
                    Result['Firebase'].add(appName)
                    Firebase = 1
                # com\yandex\metrica
                if os.path.exists(os.path.join(smaliFile,'com','yandex','metrica')) :
                    print(' --yandex') 
                    Result['yandex'].add(appName)
                    yandex = 1
                # ======================== 2023-12-21 updta
                if os.path.exists(os.path.join(smaliFile,'com','ad4screen')) :
                    print(' --ad4screen') 
                    Result['ad4screen'].add(appName)
                    ad4screen = 1
                
                if os.path.exists(os.path.join(smaliFile,'com','jiubang')) :
                    print(' --jiubang') 
                    Result['jiubang'].add(appName)
                    jiubang = 1
                # ===============================添加原版就有的字段
                if os.path.exists(os.path.join(smaliFile,'com','growingio','android','sdk')) :
                    print(' --GrowingIO')
                    growingIO = 1
                if os.path.exists(os.path.join(smaliFile,'com','sensorsdata','analytics','android','sdk')) :
                    print(' --Sensors')
                    Sensors = 1  
                if os.path.exists(os.path.join(smaliFile,'com','umeng','analytics')) :
                    print(' --Umeng')  
                    Umeng = 1
                if os.path.exists(os.path.join(smaliFile,'com','baidu','mobstat')) :
                    print(' --Baidu')  
                    Baidu = 1
                if os.path.exists(os.path.join(smaliFile,'com','talkingdata')) :
                    print(' --Talkingdata')  
                    Talkingdata = 1
                if os.path.exists(os.path.join(smaliFile,'com','zhuge','analysis')) :
                    print(' --Zhuge')   
                    Zhuge =1
                # Foreign
                if os.path.exists(os.path.join(smaliFile,'com','amplitude','api')) :
                    print(' --Amplitude') 
                    Amplitude =1
                if os.path.exists(os.path.join(smaliFile,'com','kissmetrics','sdk')) :
                    print(' --Kissmetrics')
                    Kissmetrics=1               
                if os.path.exists(os.path.join(smaliFile,'com','mixpanel','android')) :
                    print(' --Mixpanel')    
                    Mixpanel =1           
                if os.path.exists(os.path.join(smaliFile,'com','heapanalytics','android')) :
                    print(' --Heap')  
                    Heap =1
                # if os.path.exists(os.path.join(smaliFile,'paypal')) :
                #     print('paypal')  
                    # Heap =1

                # Google
                if os.path.exists(os.path.join(smaliFile,'com','google','android','gms','analytics')) :
                    print('  --GA')  
                    GA=1
                if os.path.exists(os.path.join(smaliFile,'com','google','firebase')) :
                    print('  --Firebase') 
                    Firebase = 1  
                    
                    
                    
                
        AppSdkInfo = {"appName":appName,
                "GA":GA,
                "Firebase":Firebase,
                "Umeng":Umeng,
                "sharesdk":sharesdk,
                "yandex":yandex,
                "ad4screen":ad4screen,
                "jiubang":jiubang,
                # 
                "growingIO":growingIO,
                "Sensors":Sensors,
                "Baidu":Baidu,
                "Talkingdata":Talkingdata,
                "Zhuge":Zhuge,
                
                "Amplitude":Amplitude,
                "Kissmetrics":Kissmetrics,
                "Mixpanel":Mixpanel,
                "Heap":Heap}
        
        # growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
        # Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
        totList["apps"].append(AppSdkInfo)
    # print(Result)
    return Result,totList
#   to print log


'''
{'apps':{1,2,3,4}}
to
    apps  apps2
0     1     11
1     2     12
2     3     13
3     4     14
'''    
EXCEL_PATH = './sdk2apk.xlsx'
def json2excel(appsInfoList,outputFile):
    
    # set to list
    # appsInfoList = {'apps':{1,2,3,4},
    # 'apps2':{11,12,13,14}}
    # to
    # {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13, 14]}
    for k,v in appsInfoList.items():
        appsInfoList[k]=list(v)
    print(appsInfoList)
    
    # padding
    # {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13, None], 'app3': [123, 345, None, None]}补充到最大长度
    # nested_dict = {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13],"app3":[123,345]}
    nested_dict = appsInfoList
    max_length = max(len(value) for value in nested_dict.values())
    filled_lists = {key: list(itertools.islice(itertools.chain(value, itertools.repeat(None)), max_length))
                    for key, value in nested_dict.items()}
    # print(filled_lists)
    
    df = pd.DataFrame.from_dict(filled_lists)
    print(df)
    df.to_excel(outputFile, index=False)






if __name__ == "__main__":
    
    
    appsInfoList,totList = InsertMaindianInfo()
    json2excel(appsInfoList,EXCEL_PATH)
    
    df = pd.DataFrame.from_dict(totList['apps'])
    df.to_excel('apk2sdk.xlsx', index=False)

        
    
    