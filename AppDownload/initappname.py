import re

import os
'''
由于下载当中app名和package名会包含特殊字符，需要对apk进行初步处理
目前没有直接办法从apk拿到packagename

xapk在转apk时会自动有包名，可以不管
'''

def clean_appname(appname):
    # 定义正则表达式，匹配非字母、数字、下划线、中文字符、句号的部分
    # \w 匹配字母、数字和下划线；\u4e00-\u9fa5 匹配中文字符；\. 匹配句号
    cleaned = re.sub(r'[^\w\u4e00-\u9fa5\.]', '', appname, flags=re.UNICODE)
    cleaned = re.sub(r'[\u0600-\u06FF]', '', cleaned, flags=re.UNICODE)
    cleaned = cleaned.replace(" ","")
    cleaned = cleaned.replace("_","")
    cleaned = cleaned.lower()
    return cleaned
def rename_apk_files(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件扩展名是否为 .apk
        if filename.endswith('.apk'):
            # 获取清理后的文件名
            cleaned_name = clean_appname(filename)
            # 确保文件名不为空
            if cleaned_name:
                # 构造新的文件路径
                new_filename = f"{cleaned_name}"
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                # 重命名文件
                print(f"Renaming {filename} to {new_filename}")
                os.rename(old_path, new_path)

def main():
    rename_apk_files("data/APK/")
if __name__ == '__main__':
    main()


