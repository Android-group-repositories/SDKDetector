<<<<<<< HEAD
## simple usage

```python
python ./main.py
```
DECODEAPP_FOLDER
目录下需要的是apktools -o 解包出来的文件夹

CONF_PATH存放要检测的包和匹配的特征

```python
    DECODEAPP_FOLDER = os.path.abspath(r"appDecoded[202458]/Adjust")
    CONF_PATH =  "Sdk_Featuries.json"
```

DECODEAPP_FOLDER目录结构如下

```python
(base) PS ...appDecoded[202458]\Adjust> wsl tree -L 2
.
├── com.dino.race.master
│   ├── apktool.yml
│   ├── original
│   └── unknown
├── com.easygames.race
│   ├── AndroidManifest.xml
│   ├── META-INF
│   ├── apktool.yml
│   ├── assets
│   ├── kotlin
│   ├── lib
│   ├── original
│   ├── res
│   ├── smali
│   ├── smali_assets
│   ├── smali_classes2
│   ├── smali_classes3
│   ├── smali_classes4
│   ├── smali_classes5
│   ├── smali_classes6
│   ├── smali_classes7
│   └── unknown
```


Excel文件输出1位置可以灵活设置
```python
df = pd.DataFrame.from_dict(d_result_app2sdk['app'])
    df.to_excel(r"D:\狠狠科研\hels安卓\安卓app解包分析\data\appDecoded[202458]/[2k6]apk2sdk.xlsx", index=False)
    json2excel(d_result_sdk2app,r"D:\狠狠科研\hels安卓\安卓app解包分析\data\appDecoded[202458]/[2k6]apk2sdk.xlsx/[2k6]sdk2apk.xlsx")
```