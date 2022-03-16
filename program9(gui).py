import random
import csv
from tkinter import*
from tkinter.ttk import*
from datetime import datetime
from datetime import date
root2=Tk()
root2.configure(bg="blue")
root2.title("Auto Program Generator-ISE")
root2.geometry("600x300")
stude=[['USN','Name','Program Assigned','Time']]
def textfi(pgm,rl,name):
    rn="4VV20IS"+rl.upper()
    to=str(datetime.now())
    stude.append([rn,name,pgm,to])
    root3=Tk()
    root3.title("PROGRAM DISPLAY")
    root3.configure(bg="orange")
    root3.geometry("1200x300")
    lb1=Label(root3,text="Python Laboratory-Department of ISE-Lab Internals"+"\n\n"+"\t\tYour Lab Program is- "+"\n\n"+""+pgm+
              '\n\n'+'\t\tGenerated at\t\t'+to,font="Helvetica 9 bold")
    lb1.pack()
    root3.mainloop()
    print(stude)
def gen():
    n=random.randint(1,7)
    print("Your program is",n)
    l1=["1a)Magic number 1b)Prime number","2)Rock-Paper-Scissor","3a)Extract String Between @ and # 3b)Occurence of e 3c)Removing 'the' word 3d)Counting apple","4a)String reverse\4b)All email sep ; 4c)Occurence of each character","5)Hangman game","6a)Number of words and length of each word 6b)Reverse order of fibonacci","7a)Extract Email id's from the given string\7b)Password Validity","8a)Traverse Path and Display Files and Subdirectories 8b)Read a file content and copy"]
    print(l1)
    root4=Tk()
    root4.title("Student Roll Number")
    root4.configure(bg="white")
    root4.geometry("300x200")
    roll_no=Label(root4,text="Enter student roll number")
    roll_no_g=Entry(root4)
    s_name=Label(root4,text="Enter student name")
    s_name_g=Entry(root4)
    roll_no.pack()
    roll_no_g.pack()
    s_name.pack()
    s_name_g.pack()
    bt3=Button(root4,text='OK',command=lambda:textfi(l1[n],str(roll_no_g.get()),str(s_name_g.get())))
    bt3.pack(side=TOP,pady=0)
def close():
    fname=batch_ent.get()+".csv"
    with open(fname,'w',newline='')as n_4:
        csv_writer=csv.writer(n_4,delimiter=",")
        for i in stude:
            csv_writer.writerow(i)
L1=Label(root2,text="Enter Batch")
L1.pack(side=TOP,pady=10)
batch_ent=Entry(root2)
batch_ent.pack(side=TOP,pady=10)
Bt1=Button(root2,text="Generate",command=lambda:gen())
Bt1.pack(side=TOP,pady=20)
Bt1=Button(root2,text="Done",command=lambda:close())
Bt1.pack(side=TOP,pady=20)   
Lab=Label(root2,text="Department of ISE-VVCE-Mysuru")
Lab.pack(side=BOTTOM)
root2.mainloop()