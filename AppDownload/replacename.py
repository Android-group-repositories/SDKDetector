import os
import json

# 假设你的 JSON 数据存储在一个变量中
import re


def compare_strings(s1, s2):
    # 去掉标点符号并统一为小写
    def normalize(s):
        # 去掉标点符号
        s = re.sub(r'[._:]', '', s)
        # 转换为小写
        s = s.lower()
        return s

    # 比较处理后的字符串
    return normalize(s1) == normalize(s2)

def main():
    # 文件夹路径
    folder_path = r"data\APK"

    # 用于存储未找到的文件
    failed_files = {}

    # JSON 文件路径
    json_file_path = r"data\download_info\pkgToApp.json"
    # 用于存储未找到的文件
    # failed_files = {}

    # 读取 JSON 文件
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)  # 加载 JSON 数据
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
        exit(1)

    # 遍历 JSON 数据
    for item in data:
        app_name = item["appName"]
        pkg_name = item["pkgName"]
        # 构建文件的完整路径
        old_file = os.path.join(folder_path, app_name)
        # 检查文件是否存在
        if os.path.exists(old_file):
            # 构建新的文件名
            new_file = os.path.join(folder_path, pkg_name + ".apk")
            # 重命名文件
            os.rename(old_file, new_file)
            print(f"Renamed {app_name} to {pkg_name}.apk")
        else:
            # 如果文件不存在，记录到 failed_files 字典中
            failed_files[app_name] = "File not found"
            print(f"Failed to find {app_name}")

    # 输出未找到的文件
    # 输出未找到的文件
    if failed_files:
        print("\nFiles that were not found:")
        for app_name, reason in failed_files.items():
            print(f"{app_name}: {reason}")

        # 将 failed_files 保存到 JSON 文件
        failed_files_path = os.path.join(folder_path, "failed_files.json")
        with open(failed_files_path, "w", encoding="utf-8") as f:
            json.dump(failed_files, f, indent=4, ensure_ascii=False)
        print(f"\nFailed files saved to {failed_files_path}")
    else:
        print("\nAll files were successfully renamed.")

if __name__ == '__main__':
    main()