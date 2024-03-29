from PyPDF2 import PdfReader

# 每个书签的索引格式
# {'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

file_list = ["文件名"]  # 要提取目录的pdf文件名（不包含后缀）
directory_str = ""


def bookmark_listhandler(list, level=1):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += "#" * level
            directory_str += " " + message["/Title"] + "\n"
        else:
            bookmark_listhandler(message, level + 1)


def get_bookmark(filename):
    global directory_str
    directory_str = ""
    with open(filename + ".pdf", "rb") as f:
        pdf = PdfReader(f)
        # 检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
        text_outline_list = pdf.outline
        bookmark_listhandler(text_outline_list)
    return directory_str


with open("目录.txt", "w", encoding="utf-8") as f:
    for file in file_list:
        f.write(file + "\n")
        f.write(get_bookmark(file))
        f.write("\n")
