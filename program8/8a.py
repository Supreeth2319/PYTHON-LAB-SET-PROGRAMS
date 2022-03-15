import os
print("enter the path to traverse: ")
root_dir=input()
if os.path.exists(root_dir):
    dir_count=0
    file_count=0
    for dir_name,sub_dir_list,file_list in os.walk(root_dir):
        print(dir_name)
        print("\n found directory:",dir_name)
        dir_count+=1
        for file_name in file_list:
            file_count+=1
            print("\n file name(s):",file_name)
    print("\n number of subdirectories are:",dir_count-1)
    print("\n number of files are:",file_count)
else:
    print("entered path does not exists")