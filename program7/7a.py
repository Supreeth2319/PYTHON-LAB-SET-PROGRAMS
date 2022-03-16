import re
txt=input("enter a string:")
mailid=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.\w+",txt)
print(mailid)
if mailid==[]:
    print("invalid")