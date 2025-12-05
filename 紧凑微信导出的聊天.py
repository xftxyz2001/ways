# 紧凑微信导出的聊天

import re
import pyperclip
from io import StringIO

# 日期分隔符：—— YYYY-MM-DD ——
date_line_re = re.compile(r"^—{3,}\s*\d{4}-\d{2}-\d{2}\s*—{3,}$")

# 用户行：用户名 + 时间
user_line_re = re.compile(r"^(.+?)\s+(\d{2}:\d{2})$")


def merge_chat(msg: str) -> str:
    out = StringIO()
    last_user = None

    for raw in msg.splitlines():
        line = raw.strip()
        if not line:
            continue

        # ---------- 日期行 ----------
        if date_line_re.match(line):
            if last_user is not None:
                out.write("\n")
            out.write(line + "\n")
            last_user = None
            continue

        # ---------- 用户行 ----------
        m = user_line_re.match(line)
        if m:
            user, time = m.groups()
            structured = f"{user} {time}"

            # 必须确保整行完全符合格式（避免正文误识别）
            if structured == line:
                if user != last_user:
                    if last_user is not None:
                        out.write("\n")
                    out.write(f"**{line}**\n")  # Markdown 粗体
                    last_user = user
                continue  # same user → skip this user-line

        # ---------- 普通内容 ----------
        out.write(line + "\n")

    return out.getvalue().strip()


if __name__ == "__main__":
    raw = pyperclip.paste()
    if not raw:  # 剪贴板为空
        print("剪贴板为空！")
        exit(1)

    result = merge_chat(raw)
    print(result)
    pyperclip.copy(result)
    print("\n已复制到剪贴板！")
