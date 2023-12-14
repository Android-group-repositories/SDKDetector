import os
# from dataBase import DataBase123123123
import json
from icecream import *
from DataBase import DataBase
from openpyxl import Workbook, load_workbook

import pandas as pd
def findSmaliFolder(decodeFile):
    folderList = []
    for fileName in os.listdir(decodeFile):
        if fileName.find('smali') != -1 :
            folderList.append(os.path.join(decodeFile,fileName))
    return folderList

def InsertMaindianInfo(decodeFolder):    
    totList ={"apps":[]}
    for appName in os.listdir(decodeFolder):
        decodeFile =  os.path.join(decodeFolder,appName)
        # if appName in hashInTable : 
        #     continue
        samliFiles = findSmaliFolder(decodeFile)
        growingIO = Sensors = Umeng = Baidu = Talkingdata = Zhuge = 0
        Amplitude = Kissmetrics = Mixpanel = Heap = GA =  Firebase = 0 
        print(appName)
        for smaliFile in samliFiles:
            
            if not os.path.exists(os.path.join(smaliFile,'com')):
                continue
            else :
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
#   to print log
        AppSdkInfo = {"appName":appName,"growingIO":growingIO,"Sensors":Sensors,"Umeng":Umeng,"Baidu":Baidu,"Talkingdata":Talkingdata,"Zhuge":Zhuge,"Amplitude":Amplitude,"Kissmetrics":Kissmetrics,\
                    "Mixpanel":Mixpanel,"Heap":Heap,"GA":GA,"Firebase":Firebase}
        tmp = (appName, growingIO,Sensors,Umeng,Baidu,Talkingdata,Zhuge,Amplitude,\
            Kissmetrics,Mixpanel,Heap,GA,Firebase)
        # ic(tmp)
        totList["apps"].append(AppSdkInfo)
    ic(totList)
    return totList
        # db.insert("INSERT INTO maidianInfo VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)",tmp)  

def json2excel(appsInfoList):
    df = pd.DataFrame.from_dict(appsInfoList['apps'])
    df.to_excel('data2.xlsx', index=False)





if __name__ == "__main__":
    
    
    # step2
    # elxcel 表格先放一放,这个上传飞书格式可能有问题
    # 
    
    # outputFile= "./res.xlsx"
    decodeFolder='./appDecoded'
    appsInfoList = InsertMaindianInfo(decodeFolder)
    json2excel(appsInfoList)
    
    