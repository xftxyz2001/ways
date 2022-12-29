from PyPDF2 import PdfReader as pdf_read

# 每个书签的索引格式
#{'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

filename = '1.pdf'  # 要提取目录的pdf文件名


directory_str = ''


def bookmark_listhandler(list):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += message['/Title'] + '\n'
            # print(message['/Title'])
        else:
            bookmark_listhandler(message)


with open(filename, 'rb') as f:
    pdf = pdf_read(f)
    # 检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
    text_outline_list = pdf.outline
    bookmark_listhandler(text_outline_list)

with open('directory.txt', 'w', encoding='utf-8') as f:
    f.write(directory_str)
