import re

import pyperclip

msg = """
userA  00:00

消息1

userA  00:01

消息2

userB  00:02

消息3

"""

# 上一个说话的人
last = ""

# 处理结果
res = ""

reg = re.compile(r"(.+?)\s+\d{2}:\d{2}")
# 逐行遍历
for line in msg.split("\n"):
    # 跳过空行
    if not line:
        continue

    # 如果是说话人信息行，拿到说话的人
    if reg.match(line):
        username = reg.match(line).group(1)
        # 与上一个说话的人相同
        if username == last:
            continue
        # 与上一个说话的人不同
        else:
            if last:
                res += "\n"
            last = username
            res += line + "\n"
    # 如果不是说话人信息行，拼接到上一个说话人的信息行
    else:
        res += line + "\n"

# 打印结果
print(res)
# 同步到剪切板
pyperclip.copy(res)
print("结果已同步到剪切板")
