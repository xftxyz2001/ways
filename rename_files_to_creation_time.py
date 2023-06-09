import os
import datetime
import uuid
import win32api
import win32con


def rename_files_to_creation_time(directory):
    """
    将目录中的文件重命名为它们的创建时间和唯一标识符的组合。

    Args:
        directory (str): 要重命名文件的目录路径。

    Returns:
        None

    Raises:
        OSError: 如果目录不存在或无法访问，则引发此异常。

    Example:
        >>> rename_files_to_creation_time('/path/to/directory')
    """
    # 获取脚本文件名
    script_filename = os.path.basename(__file__)
    # 遍历目录中的文件
    for filename in os.listdir(directory):
        # 获取文件路径
        path = os.path.join(directory, filename)
        # 如果是文件
        if os.path.isfile(path):
            # 获取文件的属性
            attrs = win32api.GetFileAttributes(path)
            # 如果文件没有设置隐藏属性
            if not attrs & win32con.FILE_ATTRIBUTE_HIDDEN:
                # 跳过脚本文件
                if filename == script_filename:
                    continue
                # 获取文件的创建时间
                creation_time = os.path.getctime(path)
                # 生成唯一的标识符
                unique_id = str(uuid.uuid4())[:8]
                # 生成新的文件名
                new_filename = (
                    datetime.datetime.fromtimestamp(creation_time).strftime(
                        "%Y-%m-%d %H-%M-%S"
                    )
                    + "_"
                    + unique_id
                    + os.path.splitext(filename)[1]
                )
                # 生成新的文件路径
                new_path = os.path.join(directory, new_filename)
                # 重命名文件
                print(f"Renaming {filename} to {new_filename}...")
                os.rename(path, new_path)


if __name__ == "__main__":
    rename_files_to_creation_time(os.getcwd())
