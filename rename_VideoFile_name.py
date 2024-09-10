import os

def rename_files_in_directory(directory_path):
    # 获取目录中的所有文件名
    files = os.listdir(directory_path)
    # 过滤出所有MP4文件
    mp4_files = [file for file in files if file.endswith('.mp4')]
    # 按名称排序以确保按顺序重命名
    mp4_files.sort()

    # 遍历MP4文件并重命名
    for i, file_name in enumerate(mp4_files, start=1):
        # 构造旧文件名和新文件名的完整路径
        old_file_path = os.path.join(directory_path, file_name)
        new_file_name = f"{i}.mp4"
        new_file_path = os.path.join(directory_path, new_file_name)
        
        # 检查新文件名是否已存在
        if os.path.exists(new_file_path):
            print(f"Skipped (exists): {new_file_path}")
            continue
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")

# 设置目录路径
directory_path = "./"
# 调用函数重命名文件
rename_files_in_directory(directory_path)