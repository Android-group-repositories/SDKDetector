# def highlight_word_in_text(text, word_to_highlight):
#     highlighted_text = text.replace(word_to_highlight, '\033[32m{}\033[0m'.format(word_to_highlight))
#     return highlighted_text

# text = "Hello, this is a test."
# word_to_highlight = "test"

# print(highlight_word_in_text(text, word_to_highlight))

import pandas as pd


'''
{'apps':{1,2,3,4}}
to
    apps  apps2
0     1     11
1     2     12
2     3     13
3     4     14
'''    
EXCEL_PATH = './testdata.xlsx'
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
    nested_dict = {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13],"app3":[123,345]}
    max_length = max(len(value) for value in nested_dict.values())
    filled_lists = {key: list(itertools.islice(itertools.chain(value, itertools.repeat(None)), max_length))
                    for key, value in nested_dict.items()}
    # print(filled_lists)
    
    df = pd.DataFrame.from_dict(filled_lists)
    print(df)
    df.to_excel(outputFile, index=False)

import itertools





if __name__ == "__main__":
    
    
    # step2
    outputFile= "./res.xlsx"
    decodeFolder='./appDecoded'
    # appsInfoList = InsertMaindianInfo(decodeFolder)
    appsInfoList = {'apps':{1,2,3,4},
                    'apps2':{11,12,13}}
    nested_dict = {'apps': [1, 2, 3, 4], 'apps2': [11, 12, 13],"app3":[123,345]}

    # 找出最长列表的长度
    # max_length = max(len(value) for value in nested_dict.values())

    # # 使用 zip_longest() 将所有列表填充到相同的长度
    # filled_lists = {key: list(itertools.islice(itertools.chain(value, itertools.repeat(None)), max_length))
    #                 for key, value in nested_dict.items()}
    # print(filled_lists)
    json2excel(nested_dict,EXCEL_PATH)


    
    