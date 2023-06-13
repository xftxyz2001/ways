import os
import shutil
import re

# 获取当前目录下的所有md文件
md_files = [f for f in os.listdir(".") if f.endswith(".md")]

# 遍历每个md文件
for md_file in md_files:
    # 获取md文件名（不包含扩展名）
    md_file_name = os.path.splitext(md_file)[0]
    # 创建对应的images文件夹
    os.makedirs(f"images/{md_file_name}", exist_ok=True)
    # 读取md文件内容
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    # 匹配md文件中的图片引用
    pattern = r"!\[.*\]\((.*)\)"
    matches = re.findall(pattern, content)
    # 遍历每个匹配到的图片引用
    for match in matches:
        # 获取图片文件名
        image_file_name = os.path.basename(match)
        # 移动图片文件到对应的images文件夹中
        shutil.move(match, f"images/{md_file_name}/{image_file_name}")
        # 替换md文件中的图片引用
        content = content.replace(match, f"images/{md_file_name}/{image_file_name}")
    # 将替换后的md文件内容写回文件中
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)

# 输出操作完成信息
print("所有图片已归类到对应的images文件夹中。")
