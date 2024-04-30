import json

import os
import pandas as pd
import itertools
# DEBUG = 0
DEBUG = False

def ReadConfJson(path):
    '''
    读取并处理指定路径下的 JSON 文件,提取需要检测的 SDK 信息。

    参数:
    filePath: 字符串,指定的 JSON 文件路径。

    返回值:
    一个字典,包含需要检测的 SDK 及其特征信息。

    配置文件格式:

    {
    "toDetect": [
        "umeng",
        "sharesdk"
    ],
    "sdks": {
        
        "umeng": [
            "",
            ""
        ]
    }
    }
    # 'Sdk_Featuries.json'
    '''
    
    with open(path, 'r') as file:
        json_data = file.read()

        data_dict = json.loads(json_data)
    a_toDetect = data_dict["toDetect"]
    d_rawSDks = data_dict["sdks"]
    # print(a_toDetect)
    # print(len(d_rawSDks),d_rawSDks)
    d_SDksFeaturies={}
    name_list =[ ]
    for key, value in d_rawSDks.items():
        # 使用键值对构建新的字典
        # new_dict[key] = value
        name_list.append(key)
        if(key in a_toDetect):
            d_SDksFeaturies.update({key:value})
        else:
            continue
    if(DEBUG):
        print("d_SDksFeaturies",d_SDksFeaturies)
        # print(name_list)
    # d_SDksFeaturies键值就是a_toDetect 不优化也不影响吧
    return d_SDksFeaturies,a_toDetect



def b_isIntegrated(smaliFile,SDKname,a_SDksFeaturies):
    """
    检查给定的smali文件是否包含了指定SDK的特征。
    
    参数:
    - smaliFile: 字符串,表示smali文件的路径。
    - SDKname: 字符串,表示SDK的名称,此参数在函数内未使用。
    - a_SDksFeaturies: 列表,包含了多个SDK特征的字符串表示。
    
    返回值:
    - 布尔值,如果smali文件中存在至少一个特征,则返回True,否则返回False。
    """
    
    for feature in a_SDksFeaturies:
        tmp = feature.split('.')
        # print(tmp)
        # print(os.path.join(smaliFile, * tmp))
        if os.path.exists(os.path.join(smaliFile,* tmp)):
            if(DEBUG):
                print(' --' + feature)
            # input()
            return True
    return False


def json2excel(appsInfoList,outputFile):
    
    # set to list
    # appsInfoList = {'apps':{1,2,3,4},
    # 'apps2':{11,12,13,14}}
    # to
    # {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13, 14]}
    for k,v in appsInfoList.items():
        appsInfoList[k]=list(v)
    if(DEBUG):
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
    # if(DEBUG):
    print(df)
    df.to_excel(outputFile, index=False)


def findSmaliFolder(Appdir):
    """
    寻找指定目录下的所有包含 'smali' 字段的文件夹。
    
    参数:
    Appdir (str): 指定的搜索目录路径。
    
    返回:
    list: 包含所有找到的含有 'smali' 字段的文件夹路径的列表。
    """
    folderList = []
    for fileName in os.listdir(Appdir):
        if fileName.find('smali') != -1 :
            folderList.append(os.path.join(Appdir,fileName))
    return folderList

def CheckAllApk(CONF_PATH,DECODEAPP_FOLDER):

    # DECODEAPP_FOLDER = os.path.abspath(r"D:\狠狠科研\hels安卓\安卓app解包分析\data\appDecoded测试")

    # CONF_PATH =  "D:\狠狠科研\hels安卓\安卓app解包分析\main\Sdk_Featuries.json"
    d_SDksFeaturies,a_toDetect = ReadConfJson(CONF_PATH)


    d_result_app2sdk = {"app":[]}
    d_isIntegrated={}
    d_result_sdk2app = {}

    # init
    for key, value in d_SDksFeaturies.items():
        d_isIntegrated[key]=0
        d_result_sdk2app[key]=[]
    # print(d_isIntegrated)
    # print(d_result_sdk2app)



    # DECODEAPP_FOLDER = os.path.abspath(r"D:\狠狠科研\hels安卓\安卓app解包分析\data\appDecoded测试")
    for appName in os.listdir(DECODEAPP_FOLDER):
        d_isAPPIntegrated = d_isIntegrated
        
        Appdir =  os.path.join(DECODEAPP_FOLDER,appName)
        # print(Appdir)
        a_samliFiles = findSmaliFolder(Appdir)
        # print(a_samliFiles)
        
        # print(appName)
        
            
        for smaliFile in a_samliFiles:
            # 有的sdk路径根本就不包含com吧？？？
            # if not os.path.exists(os.path.join(smaliFile,'com')):
            #     continue
            # else :
            for SDKname in a_toDetect:
                if( b_isIntegrated(smaliFile,SDKname,d_SDksFeaturies[SDKname])):
                    # app 集成 某SDK
                    d_isAPPIntegrated[SDKname]=1
                    d_result_sdk2app[SDKname].append(appName)
                        
            # print(d_isAPPIntegrated)
        
        # 由于pandas特性 必须手动加入一个表头。。。。
        
        # d_isAPPIntegrated.update({"appName" :appName})
        d_isAPPIntegrated = {"appName" :appName, **d_isAPPIntegrated}
        d_result_app2sdk['app'].append(d_isAPPIntegrated)
    # ==================================================================
    # print(d_result_sdk2app)
    # json2excel(d_result_sdk2app,'./sdk2apk.xlsx')
    return d_result_sdk2app,d_result_app2sdk

# print(d_result_sdk2app)
# df = pd.DataFrame.from_dict(d_result_app2sdk['app'])
# df.to_excel('apk2sdk.xlsx', index=False)
def main():
    DECODEAPP_FOLDER = os.path.abspath(r"D:\狠狠科研\hels安卓\安卓app解包分析\data\appDecoded测试")
    
    # json 配置文件 
    CONF_PATH =  "D:\狠狠科研\hels安卓\安卓app解包分析\main\Sdk_Featuries.json"
    d_result_sdk2app,d_result_app2sdk = CheckAllApk(CONF_PATH,DECODEAPP_FOLDER)
    if(DEBUG):
        print(d_result_sdk2app)
    df = pd.DataFrame.from_dict(d_result_app2sdk['app'])
    df.to_excel('./apk2sdk.xlsx', index=False)
    json2excel(d_result_sdk2app,'./sdk2apk.xlsx')
    
    
    
    
    
if __name__ == "__main__":
    main()