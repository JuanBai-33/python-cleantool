
import os
import shutil
import ctypes


CLEAN_PATHS = [
    
    r"C:\Windows\Temp",
   
    os.path.expandvars(r"%TEMP%"),
    
    r"C:\Windows\SoftwareDistribution\Download",
   
    r"C:\Windows\Logs",
]


total_files = 0
total_size = 0

def get_file_size(path):
     return os.path.getsize(path)

def clean_folder(folder_path):
    global total_files, total_size

    if not os.path.exists(folder_path):
        print(f"【不存在】{folder_path}")
        return

    print(f"\n开始清理：{folder_path}")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path):
                size = get_file_size(item_path)
                os.remove(item_path)
                total_files += 1
                total_size += size
                print(f"删除文件：{item}")

            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                total_files += 1
                print(f"删除文件夹：{item}")

        except Exception as e:  
            continue

def main():
    print("C盘安全清理工具")
    print("仅清理系统临时垃圾，不会删除系统核心文件\n")

    for path in CLEAN_PATHS:
        clean_folder(path)

    
    mb = total_size / 1024 / 1024
    print("\n--------------------------------")
    print(f"清理完成！")
    print(f"总共清理文件数：{total_files} 个")
    print(f"释放磁盘空间：{mb:.2f} MB")
    print("----------------------------------")

if __name__ == "__main__":
    main()
    