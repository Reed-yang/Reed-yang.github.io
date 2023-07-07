import os
import shutil
import stat
import time

def copy_directory_files_with_create_time(source_dir, destination_dir):
    # 遍历源目录下的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)  # 源文件路径
            dest_file = os.path.join(destination_dir, os.path.relpath(source_file, source_dir))  # 目标文件路径
            
            # 获取源文件的创建时间
            st = os.stat(source_file)
            create_time = st.st_ctime

            # 拷贝文件
            shutil.copy2(source_file, dest_file)

            # 设置目标文件的创建时间
            os.utime(dest_file, (create_time, create_time))

# 示例用法
source_directory = 'C:\\Users\\Reedyoung\\Box\\MDs'
destination_directory = 'D:\\Hugo\\Reed-yang.github.io\\content\\posts'
copy_directory_files_with_create_time(source_directory, destination_directory)
