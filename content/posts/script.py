# 编写一个python脚本，实现如下功能：
# 1. 对当前目录所有.md文件进行处理，如果存在文件夹则递归遍历所有的子文件夹
# 2. 对于每个.md文件，检查文件头是否包含YAML Front Matter，如果没有则添加"文件名"为tile的YAML Front Matter
# 3. 对于每个.md文件，检查文件头是否包含"date"，如果没有则添加"文件名"为date的YAML Front Matter，值为文件的创建时间
# 4. 对于每个.md文件，检查文件头是否包含"tags"，如果没有则添加"文件名"为tags的YAML Front Matter，值为文件的父文件夹名
# 5. 对于每个.md文件，检查文件中以html语法插入的图片链接(形如<img src="xxx" alt="xxx" style="zoom:xxx"/>)，为其添加"margin: 0 auto;"实现居中显示添加后应该形如(形如<img src="xxx" alt="xxx" style="zoom:xxx;margin: 0 auto;"/>),而且要确保不会重复添加

import os
import re
import datetime
import win32file




def detect_yaml_front_matter(content):
    match = re.match(r'---\s*(.*?)\s*---', content, re.DOTALL)
    if match:
        return match.group(1).rstrip() + '\n'
    return None

def process_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_md_file(file_path)

def process_YAML_front_matter(yaml_front_matter, file_path):
        data = True
        tags = True
        toc = True
        

        # 检查是否存在date字段
        if data and 'date' not in yaml_front_matter:

            # handle = win32file.CreateFile(
            #     file_path,
            #     win32file.GENERIC_READ,
            #     win32file.FILE_SHARE_READ,
            #     None,
            #     win32file.OPEN_EXISTING,
            #     0,
            #     None
            # )

            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            # creation_time = win32file.GetFileTime(handle)[0]
            # win32file.CloseHandle(handle)
            # create_datetime = datetime.datetime.fromtimestamp(creation_time)
            creation_time_str = creation_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            yaml_front_matter += f"date: {creation_time_str}\n"

        # 检查是否存在tags字段
        if tags and 'tags' not in yaml_front_matter:
            parent_folders = os.path.dirname(file_path).split(os.path.sep)
            tags = [folder for folder in parent_folders if folder != '.']
            if not tags:
                tags = ['uncategorized']
            yaml_front_matter += f"tags: {tags}\n"
        return yaml_front_matter


def process_md_file(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()

        # 检测是否存在YAML Front Matter
        yaml_front_matter = detect_yaml_front_matter(content)

        # 如果不存在YAML Front Matter，则添加默认的Front Matter
        if not yaml_front_matter:
            yaml_front_matter = f"title: \"{os.path.splitext(os.path.basename(file.name))[0]}\"\n"

        yaml_front_matter = process_YAML_front_matter(yaml_front_matter, file_path)

        # 更新图片链接的样式 且 防止重复
        updated_content = re.sub(r'<img src="(.*?)" alt="(.*?)" style="zoom:(.*?);" />',
                                lambda match: '<img src="{}" alt="{}" style="zoom:{};{}" />'.format(
                                    match.group(1), match.group(2), match.group(3),
                                    'margin: 0 auto;' if 'margin' not in match.group(3) else ''),
                                content)

        # 删除原有的YAML Front Matter 和 空行
        updated_content = re.sub(r'^\s*---\s*(.*?)\s*---', '', updated_content, flags=re.DOTALL)
        updated_content = re.sub(r'^\s*$', '', updated_content, flags=re.MULTILINE)
        # 将更新后的内容重新写入文件
        file.seek(0, 0)
        file.write(f"---\n{yaml_front_matter}---\n{updated_content}")

        file.truncate()

# 在当前目录下处理所有.md文件（包括子文件夹）
process_md_files('.')
