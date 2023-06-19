#!/bin/bash

# 递归遍历文件夹中的所有 .md 文件
function process_files() {
    for file in "$1"/*; do
        # 如果是目录，则递归处理该目录下的文件
        if [[ -d "$file" ]]; then
            process_files "$file"
        # 如果是普通文件且扩展名为 .md
        elif [[ -f "$file" && "${file##*.}" == "md" ]]; then
            # 提取文件名（不包括扩展名）
            filename=$(basename "$file" .md)
            # 对首个非空行检查是否为 YAML front matter，不是则返回 1，赋值给 flag
            grep -m 1 -v '^$' "$file" | grep -q '^---$'; flag=$(echo $?)
            # 检查文件是否已经包含 YAML front matter
            if [ "$flag" -eq 1 ] ; then
                # 生成 YAML front matter
                front_matter="---\ntitle: \"$filename\"\n---\n"

                # 将 YAML front matter 插入到文件的开头
                echo -e "$front_matter$(cat "$file")" > "$file"
                echo "为文件 $file 生成 YAML front matter。"
            else
                echo "文件 $file 已包含 YAML front matter。"
            fi
        fi
    done
}

# 指定要处理的根文件夹路径
root_folder="./"

# 调用函数处理文件夹及其子文件夹中的 .md 文件
process_files "$root_folder"


