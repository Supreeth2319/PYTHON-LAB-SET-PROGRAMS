import os
input_file=input("enter the text path ")
output_file=input("enter the path where content should be copied: ")
if os.path.exists(input_file)&os.path.exists(output_file):
    print("valid path")
    file=open(input_file,'r')
    lines=file.readlines()
    newfile=open(output_file,'w')
    print("odd lines are copied")
    for i in range(0,len(lines),2):
        newfile.write(lines[i])
        print(lines[i])
    file.close()
    newfile.close()
else:
    print("not a valid path")