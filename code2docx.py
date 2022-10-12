import os
import sys

suffix = ['py']  # 要处理的代码的后缀名（不包含.）
exclude = []  # 要排除的文件名（包含扩展名）

with open('code.md', 'w', encoding='utf-8') as f:
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            file_suffix = filename.split('.')[-1]
            if file_suffix in suffix:
                if filename == sys.argv[0].split(os.sep)[-1] or filename in exclude:
                    continue
                f.write(filename + '\n```' + file_suffix + '\n')
                with open(filename, 'r', encoding='utf-8') as f2:
                    f.write(f2.read())
                f.write('\n```\n\n')

os.system('pandoc code.md -o code.docx')
