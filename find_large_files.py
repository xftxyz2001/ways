import os
from pathlib import Path

def find_largest_files(directory, num_files=10):
    """查找目录中最大的N个文件"""
    file_sizes = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                file_sizes.append((file_path, size))
            except (OSError, FileNotFoundError):
                continue
    
    # 按文件大小降序排序
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    
    return file_sizes[:num_files]

if __name__ == "__main__":
    # 当前工作目录
    directory = "."
    
    print(f"查找目录: {os.path.abspath(directory)}\n")
    print(f"{'文件名':<80} {'大小':>12}")
    print("=" * 100)
    
    largest_files = find_largest_files(directory, 10)
    
    for file_path, size in largest_files:
        # 转换大小为合适的单位
        if size >= 1024 * 1024:  # MB
            size_str = f"{size / (1024 * 1024):.2f} MB"
        elif size >= 1024:  # KB
            size_str = f"{size / 1024:.2f} KB"
        else:  # Bytes
            size_str = f"{size} B"
        
        print(f"{file_path:<80} {size_str:>12}")
