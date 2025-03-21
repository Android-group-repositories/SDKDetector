import zipfile
import os


def extract_biggest_files_from_zip(zip_file_path, target_directory):

    # 创建目标目录（如果不存在）
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 打开 ZIP 文件
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        '''
        直接保留最大的非配置包
        过于依赖特征，另外找办法吧。。。
        '''
        file_list = zip_ref.namelist()
        apk_files = [f for f in file_list if f.lower().endswith('.apk')]

        if not apk_files:
            print("未找到任何 .apk 文件。")
            return


        largest_file = None
        largest_size = 0
        # Iterate through the list to find the largest file
        for file in apk_files  :
            file_size = zip_ref.getinfo(file).file_size
            if file_size > largest_size and "config" not in file and "asset" not in file:
                largest_size = file_size
                largest_file = file
        # Extract the largest file
        if largest_file:
            zip_ref.extract(largest_file, target_directory)

            original_path = os.path.join(target_directory, largest_file)
            new_path = os.path.join(target_directory, largest_file)
            os.rename(original_path, new_path)

            print(f"已提取文件: {largest_file} -> {target_directory}")
        else:
            print(zip_file_path,'出错')

        # # 遍历 ZIP 文件中的所有文件
        # for file in zipf.namelist():
        #     # 检查文件扩展名是否匹配
        #     if package_name in file:
        #         # 构建目标文件路径
        #         target_file_path = os.path.join(target_directory, os.path.basename(file))
        #
        #         # 提取文件到目标目录
        #         zipf.extract(file, target_directory)
        #
        #         print(f"已提取文件: {file} -> {target_file_path}")


# 示例用法


import os


def list_xapk_files_recursively(folder_path):
    """
    递归读取指定文件夹及其子文件夹下的所有 .xapk 文件并返回一个列表

    :param folder_path: 文件夹路径
    :return: 包含所有 .xapk 文件路径的列表
    """
    xapk_files = []

    # 使用 os.walk 递归遍历文件夹
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".xapk"):
                file_path = os.path.join(root, file)
                xapk_files.append(file_path)

    return xapk_files


# 示例用法
folder_path = "data/XAPK"  # 替换为你的文件夹路径
xapk_list = list_xapk_files_recursively(folder_path)

def xapk2apk_byFileSzie(folder_path = "data/XAPK"):
      # 替换为你的文件夹路径
    xapk_list = list_xapk_files_recursively(folder_path)

    print("XAPK 文件列表:")
    for i in range(len(xapk_list)):
        file = xapk_list[i]
        file_name = os.path.split(file)[1]
        print(file_name, i)
        zip_file_path = file  # ZIP 文件路径
        target_directory = "data/XAPK/extracted"  # 提取后文件存放的目录

        package_name = file_name.rsplit('.', 1)[0]
        # print(package_name)
        # input()
        extract_biggest_files_from_zip(zip_file_path, target_directory)


def xapk2apk_byPackageName(folder_path="data/XAPK"):
    #TODO
    # 现在有点冗杂，两个功能，依据包名提取，和依据文件大小提取，重复的地方直接耦合到一起
    # 替换为你的文件夹路径
    pass
    xapk_list = list_xapk_files_recursively(folder_path)

    print("XAPK 文件列表:")
    for i in range(len(xapk_list)):
        file = xapk_list[i]
        file_name = os.path.split(file)[1]
        print(file_name, i)
        zip_file_path = file  # ZIP 文件路径
        target_directory = "data/XAPK/extracted"  # 提取后文件存放的目录

        package_name = file_name.rsplit('.', 1)[0]
        # print(package_name)
        # input()
        # extract_biggest_files_from_zip(zip_file_path, target_directory, package_name)


def main():
    folder_path = "data/XAPK"
    xapk2apk_byFileSzie(folder_path)


if __name__ == '__main__':
    main()
# 打印结果