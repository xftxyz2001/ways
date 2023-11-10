import hashlib
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

md5diff, onlyInA, onlyInB = None, None, None  # 全局变量，用于存储比较结果


# 获取文件的MD5值
def getFileMd5(filename):
    if not os.path.isfile(filename):
        print("文件不存在: " + filename)
        return
    myhash = hashlib.md5()
    f = open(filename, "rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


# 获得文件夹下所有文件的相对路径
def getAllFiles(path, ignore_hidden):
    flist = []
    for root, dirs, fs in os.walk(path):
        if ignore_hidden:
            fs = [f for f in fs if not f.startswith(".")]
            dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in fs:
            f_fullpath = os.path.join(root, f)
            f_relativepath = f_fullpath[len(path) :]
            flist.append(f_relativepath)

    return flist


# 比较两个文件夹下的文件是否相同
def dirCompare(pathA, pathB, ignore_hidden):
    global md5diff, onlyInA, onlyInB
    afiles = getAllFiles(pathA, ignore_hidden)
    bfiles = getAllFiles(pathB, ignore_hidden)
    setA = set(afiles)
    setB = set(bfiles)

    # 处理共有文件
    commonfiles = setA & setB
    md5diff = []
    for of in sorted(commonfiles):
        amd = getFileMd5(pathA + "\\" + of)  # \\兼容处理
        bmd = getFileMd5(pathA + "\\" + of)
        if amd != bmd:
            md5diff.append(of)

    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB
    onlyInA = []
    onlyInB = []
    for of in onlyFiles:
        if of in afiles:
            onlyInA.append(of)
        elif of in bfiles:
            onlyInB.append(of)

    # return md5diff, onlyInA, onlyInB


# 回调：选择文件夹
def select_directory(entry):
    folder_selected = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(tk.END, folder_selected)


# 回调：比较两个文件夹
def compare_directories(entry1, entry2, text, ignore_hidden):
    global md5diff, onlyInA, onlyInB
    text.delete(1.0, tk.END)
    dir1 = entry1.get()

    if not os.path.exists(dir1):
        messagebox.showinfo("提示", "文件夹1不存在")
        return

    dir2 = entry2.get()
    if not os.path.exists(dir2):
        messagebox.showinfo("提示", "文件夹2不存在")
        return

    if dir1 == dir2:
        messagebox.showinfo("提示", "请选择不同的文件夹")
        return

    # md5diff, onlyInA, onlyInB = dirCompare(dir1, dir2, ignore_hidden)
    dirCompare(dir1, dir2, ignore_hidden)
    if len(md5diff) > 0:
        text.insert(tk.END, "-" * 20 + "共有文件" + "-" * 20 + "\n")
        for of in md5diff:
            text.insert(tk.END, of + "\n")

    if len(onlyInA) > 0:
        text.insert(tk.END, "-" * 17 + "只存在于文件夹1" + "-" * 17 + "\n")
        for of in sorted(onlyInA):
            text.insert(tk.END, of + "\n")
    if len(onlyInB) > 0:
        text.insert(tk.END, "-" * 17 + "只存在于文件夹2" + "-" * 17 + "\n")
        for of in sorted(onlyInB):
            text.insert(tk.END, of + "\n")

    messagebox.showinfo("提示", "比较完成")


# 回调：导出文本
def export_text(text):
    file_name = filedialog.asksaveasfilename(
        defaultextension=".txt",
        initialdir=os.path.expanduser("~/Desktop"),
        initialfile="output.txt",
    )
    if file_name:
        with open(file_name, "w") as file:
            file.write(text.get("1.0", tk.END))


# 回调：覆盖文件夹
def overwrite_dir(src_entry, dst_entry, file_list, text):
    global md5diff
    file_list.extend(md5diff)

    src_dir = src_entry.get()
    dst_dir = dst_entry.get()
    if messagebox.askokcancel("警告", f"确定要将{src_dir}的内容复制到{dst_dir}吗？"):
        text.insert(tk.END, "-" * 20 + "开始复制" + "-" * 20 + "\n")
        for file in file_list:
            src_file = src_dir + "\\" + file
            dst_file = dst_dir + "\\" + file
            if os.path.exists(dst_file):
                os.rename(dst_file, dst_file + ".bak")
                text.insert(tk.END, f"备份{dst_file} -> {dst_file}.bak\n")
            shutil.copy2(src_file, dst_file)
            text.insert(tk.END, f"复制{src_file} -> {dst_file}\n")


# 拖拽功能
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD

    dnd_available = True
except ImportError:
    print("tkinterdnd2库未安装，将不提供拖拽功能")
    dnd_available = False


def drop(event):
    entry = event.widget
    entry.delete(0, tk.END)
    entry.insert(tk.END, event.data)


# 窗体绘制与事件绑定
root = tk.Tk() if not dnd_available else TkinterDnD.Tk()

entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=0)
if dnd_available:
    entry1.drop_target_register(DND_FILES)
    entry1.dnd_bind("<<Drop>>", drop)

button1 = tk.Button(root, text="选择文件夹1", command=lambda: select_directory(entry1))
button1.grid(row=0, column=1)

entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=0)
if dnd_available:
    entry2.drop_target_register(DND_FILES)
    entry2.dnd_bind("<<Drop>>", drop)

button2 = tk.Button(root, text="选择文件夹2", command=lambda: select_directory(entry2))
button2.grid(row=1, column=1)

text = tk.Text(root, height=20)
text.grid(row=3, column=0, columnspan=2)

ignore_hidden = tk.IntVar(value=1)  # 默认勾选
check_button = tk.Checkbutton(root, text="忽略隐藏文件", variable=ignore_hidden)
check_button.grid(row=2, column=0)

compare_button = tk.Button(
    root,
    text="比较",
    command=lambda: compare_directories(entry1, entry2, text, ignore_hidden.get()),
    height=2,
    width=20,
)
compare_button.grid(row=2, column=1)

# 底部的按钮
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0)

overwrite_A_to_B_button = tk.Button(
    button_frame,
    text="文件夹1->文件夹2",
    command=lambda: overwrite_dir(entry1, entry2, onlyInA, text),
)
overwrite_A_to_B_button.pack(side=tk.LEFT, padx=20)

overwrite_B_to_A_button = tk.Button(
    button_frame,
    text="文件夹1<-文件夹2",
    command=lambda: overwrite_dir(entry2, entry1, onlyInB, text),
)
overwrite_B_to_A_button.pack(side=tk.LEFT)

export_button = tk.Button(root, text="导出文本", command=lambda: export_text(text))
export_button.grid(row=4, column=1)

root.title("目录比较工具 By: 通晓宇宙")
root.mainloop()

# 参考：https://blog.csdn.net/u013654125/article/details/120889716
