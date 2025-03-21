import json
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import openpyxl
import time

import io
import sys
from urllib.parse import urlparse, unquote


def getName(url):
    parsed_url = urlparse(url)
    path = parsed_url.path

    filename = path.split("/")[-1]
    filename = unquote(filename)

    directory = path.split("/")[1]
    return {"pkgName": directory, "appName": filename}


def download(lines):
    # filePath = "final_list.json"
    # f = open(filePath, 'r')
    # app_list = json.load(f)
    # f.close()

    count = 0
    name_List = []
    fail_list = []

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    # selenium初始参数设置
    ser = Service("src/AppDownload/chrome-win64/chromedriver.exe")
    op = webdriver.ChromeOptions()
    prefs = {'download.default_directory': r"E:\TOSvsPP\data\APK",  # 存储位置
             "download.prompt_for_download": False,
             'profile.default_content_settings.popups': 0,  # 设置为0，禁止弹出窗口
             "safebrowsing.enabled": True
             }

    op.add_experimental_option('prefs', prefs)
    op.add_argument("--disable-gpu")
    op.add_argument('--ignore-certificate-errors')
    print(type(ser))
    driver = webdriver.Chrome(service=ser, options=op)

    for i in range(len(lines)):  # key is name
        package = lines[i]
        url = "https://apkcombo.com/de-de/apk-downloader/?device=&arches=&sa=1&lang=en&dpi=480&q=" + package
        # https://apkcombo.com/de-de/apk-downloader/?device=&arches=&sa=1&lang=en&dpi=480&q=com.facebook.lite

        # get url
        try:
            driver.get(url)
        except Exception:
            fail_list.append(package)
            print(package + " not downloaded")
            print("get url fail")

            continue

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "file-list"))
            )  # 等动态链接被输出
        except Exception:
            fail_list.append(str(i)+"  "+package)
            print(package + " not downloaded")

            print("WebDriverWait fail")
            continue

        # 获取下载链接
        element = driver.find_element("xpath", '//*[@id="apkcombo-tab"]/div/ul[1]/li/ul/li/a')
        version = driver.find_element("xpath", '//*[@id="download-result"]/div[1]/div[2]/div[1]')

        apk_link = element.get_attribute('href')  # 获得 apk 链接

        if (apk_link.find("gcdn.androidcombo.com") == -1 and apk_link.find("fp=") == -1):
            try:
                driver.get(apk_link)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "file-list")))  # 等动态链接被输出
            except Exception:
                fail_list.append(package)
                print(package + " not downloaded")
                print("com find fail")
                continue

            element = driver.find_element("xpath", '//*[@id="best-variant-tab"]/div[1]/ul/li/ul/li/a')
            apk_link = element.get_attribute('href')  # 更新apk链接

        # 获取apk
        try:
            driver.get(apk_link)
            print(apk_link)
            name_List.append(getName(apk_link))
        except Exception:
            fail_list.append(package)
            print(package + " not downloaded")
            print("com find fail")
            continue

        count += 1
        print(package + " downloaded", flush=True)
        time.sleep(5)

    # =========================

    print(count)
    print(name_List)
    time.sleep(5)

    # 完成下载请求后第一时间关闭浏览器可能会造成未完成的下载任务中断
    # driver.quit()
    return fail_list, name_List


if __name__ == '__main__':
    lines = []

    with open(r"data\download_info\nameList.txt", "r") as file:
        for line in file:
            # 去除行尾的换行符
            line = line.rstrip("\n")
            lines.append(line)

    print(lines)
    print("pkgs = ", len(lines))
    # input("Press Enter to continue...")
    time.sleep(5)
    fail_list, name_List = download(lines)

    # log 获取下载失败的包
    with open(r"data\download_info\fail_list.txt", "w") as file:
        for package in fail_list:
            file.write(package + "\n")

    # 映射apk名与pkg名
    with open(r"data\download_info\pkgToApp.json", "w") as file:
        json.dump(name_List, file)

