
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
    
    Result = {"umeng":set(),
            "sharesdk":set(),
            "Firebase":set(),
            'yandex':set(),
            "GA":set(),
            "ad4screen":set(),
            "jiubang":set(),
            "kissmetrics":set(),
            "mixpanel":set(),
            "Heap":set(),
            "GrowingIO":set(),
            "Sensors":set(),
            "baidu":set(),
            "talkingdata":set(),
            "zhuge":set(),
            "amplitude":set(),
            # 4
            "twitter":set(),
            "bytedance":set(),
            "ironsource":set(),
            
            #3
            "onesignal":set(),
            
            "vungle":set(),
            "squareup":set(),
            "kakao":set(),
            # 2
            "applovin":set(),
            "amazon":set(),
            "startapp":set(),
            "appsflyer":set(),
            
            # 1
            "tapjoy":set(),
            "dropbox":set(),
            "unity3d":set(),
            }
    
    for appName in os.listdir(DECODE_FOLDER):
        umeng = GA = Firebase = sharesdk = yandex =jiubang=ad4screen=0
        
        growingIO = Sensors = umeng = baidu = talkingdata = zhuge = 0
        amplitude = kissmetrics = mixpanel = Heap = GA =  Firebase = 0 
        
        # tos4
        twitter = bytedance=ironsource =0
        
        # tos3
        onesignal= vungle=squareup=kakao=0 
        
        #tos2
        applovin =amazon= startapp=appsflyer=0
        
        # tos
        tapjoy = dropbox=unity3d=0
        
        # example output: "appDecoded\com.q1.knifesling"
        Appdir =  os.path.join(DECODE_FOLDER,appName)
        samliFiles = findSmaliFolder(Appdir)
        
        print()
        print(appName)
        for smaliFile in samliFiles:
            # 检查是否存在 "appDecoded\com.q1.knifesling\com"
            if not os.path.exists(os.path.join(smaliFile,'com')):
                continue
            else :
                
                # 千万别动，真不想改了
                # com.umeng.socialize.txt
                # 检查是否存在 "appDecoded\com.q1.knifesling\com\umeng\xxxxxx"
                if os.path.exists(os.path.join(smaliFile,'com','umeng','socialize')) :
                    # print(os.path.join(smaliFile,'com','umeng','analytics'))
                    print(' --umeng socialize')  
                    
                    Result['umeng'].add(appName)
                    umeng = 1
                    
                if os.path.exists(os.path.join(smaliFile,'com','umeng','analytics')) :
                    # print(os.path.join(smaliFile,'com','umeng','analytics'))
                    print(' --umeng analytics') 
                    Result['umeng'].add(appName)
                    umeng = 1
                
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
                    Result['GrowingIO'].add(appName)
                    print(' --GrowingIO')
                    growingIO = 1
                # if os.path.exists(os.path.join(smaliFile,'com','sensorsdata','analytics','android','sdk')) :
                #     print(' --Sensors')
                #     Result['sensorsdata'].add(appName)
                #     Sensors = 1  
                if os.path.exists(os.path.join(smaliFile,'com','umeng','analytics')) :
                    print(' --umeng')  
                    Result['umeng'].add(appName)
                    umeng = 1
                if os.path.exists(os.path.join(smaliFile,'com','baidu','mobstat')) :
                    print(' --baidu')  
                    Result['baidu'].add(appName)
                    baidu = 1
                if os.path.exists(os.path.join(smaliFile,'com','talkingdata')) :
                    print(' --talkingdata')  
                    Result['talkingdata'].add(appName)
                    talkingdata = 1
                if os.path.exists(os.path.join(smaliFile,'com','zhuge','analysis')) :
                    print(' --zhuge')   
                    Result['zhuge'].add(appName)
                    zhuge =1
                # Foreign
                if os.path.exists(os.path.join(smaliFile,'com','amplitude','api')) :
                    print(' --amplitude') 
                    Result['amplitude'].add(appName)
                    amplitude =1
                if os.path.exists(os.path.join(smaliFile,'com','kissmetrics','sdk')) :
                    print(' --kissmetrics')
                    Result['kissmetrics'].add(appName)
                    kissmetrics=1               
                if os.path.exists(os.path.join(smaliFile,'com','mixpanel','android')) :
                    print(' --mixpanel')    
                    Result['mixpanel'].add(appName)
                    mixpanel =1           

            
                
                # tos清单补全计划tos4 =======================================================================
                # com\twitter
                if os.path.exists(os.path.join(smaliFile,'com','twitter')) :
                    print('  --twitter') 
                    Result['twitter'].add(appName)
                    Firebase = 1  
                # \com\bytedance
                if os.path.exists(os.path.join(smaliFile,'com','bytedance')) :
                    print('  --bytedance') 
                    Result['bytedance'].add(appName)
                    Firebase = 1

                # com\ironsource
                if os.path.exists(os.path.join(smaliFile,'com','ironsource')) :
                    print('  --ironsource') 
                    Result['ironsource'].add(appName)
                    ironsource = 1
                ## tos3 =======================================================================
                # com\onesignal
                if os.path.exists(os.path.join(smaliFile,'com','onesignal')) :
                    print('  --onesignal') 
                    Result['onesignal'].add(appName)
                    onesignal = 1
                
                # com\vungle
                if os.path.exists(os.path.join(smaliFile,'com','vungle')) :
                    print('  --vungle') 
                    Result['vungle'].add(appName)
                    vungle = 1
                # com\squareup
                if os.path.exists(os.path.join(smaliFile,'com','squareup')) :
                    print('  --squareup') 
                    Result['squareup'].add(appName)
                    squareup = 1
                # com\kakao
                if os.path.exists(os.path.join(smaliFile,'com','kakao')) :
                    print('  --kakao') 
                    Result['kakao'].add(appName)
                    kakao = 1
                    
                    
                # tos2 =======================================================================
                # com\applovin
                if os.path.exists(os.path.join(smaliFile,'com','applovin')) :
                    print('  --applovin') 
                    Result['applovin'].add(appName)
                    sharesdk = 1
                    
                # com\amazon
                if os.path.exists(os.path.join(smaliFile,'com','amazon')) :
                    print('  --amazon') 
                    Result['amazon'].add(appName)
                    amazon = 1
                    
                # com\startapp
                if os.path.exists(os.path.join(smaliFile,'com','startapp')) :
                    print('  --startapp') 
                    Result['startapp'].add(appName)
                    startapp = 1
                # com\appsflyer
                if os.path.exists(os.path.join(smaliFile,'com','appsflyer')) :
                    print('  --appsflyer') 
                    Result['appsflyer'].add(appName)
                    appsflyer = 1
                # tos1=======================================================================
                
                # com\tapjoy
                if os.path.exists(os.path.join(smaliFile,'com','tapjoy')) :
                    print('  --tapjoy') 
                    Result['tapjoy'].add(appName)
                    tapjoy = 1    
                # com\dropbox
                if os.path.exists(os.path.join(smaliFile,'com','dropbox')) :
                    print('  --dropbox') 
                    Result['dropbox'].add(appName)
                    dropbox = 1
                    
                # com\unity3d\ads
                if os.path.exists(os.path.join(smaliFile,'com','unity3d','ads')) :
                    print('  --unity3d') 
                    Result['unity3d'].add(appName)
                    unity3d = 1
                
        AppSdkInfo = {"appName":appName,
                "GA":GA,
                "Firebase":Firebase,
                "umeng":umeng,
                "sharesdk":sharesdk,
                "yandex":yandex,
                "ad4screen":ad4screen,
                "jiubang":jiubang,
                # 
                "growingIO":growingIO,
                "Sensors":Sensors,
                "baidu":baidu,
                "talkingdata":talkingdata,
                "zhuge":zhuge,
                
                "amplitude":amplitude,
                "kissmetrics":kissmetrics,
                "mixpanel":mixpanel,
                "Heap":Heap,
                # tos4
                "twitter":twitter,
                "bytedance":bytedance,
                "onesignal":onesignal,
                # tos3
                "vungle":vungle,
                "ironsource":ironsource,
                "squareup":squareup,
                "kakao":kakao,
                # tos2
                "applovin":applovin,
                "amazon":amazon,
                "startapp":startapp,
                "appsflyer":appsflyer,
                # tos1
                "tapjoy":tapjoy,
                "dropbox":dropbox,
                "unity3d":unity3d
                
                }
        
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

        
    
    