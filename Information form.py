#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     01/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.title("Data Add Form")
root.geometry("500x350")

def getvals():
    print("Accepted")

#Heading

Label(root, text="Python Registration Form" , font=("Arial", 16, "bold")).grid(row=0,column=3)


#Fields
name= Label(root,text="Name").grid(row=2,column=2)
gender= Label(root,text="Gender").grid(row=4,column=2)
phone= Label(root,text="Phone").grid(row=6,column=2)
email= Label(root,text="Email").grid(row=8,column=2)
password= Label(root,text="Password").grid(row=10,column=2)
Payment= Label(root,text="Payment Method").grid(row=12,column=2)

# variable for storing data
namevalue= StringVar
gendervalue= StringVar
phonevalue= StringVar
emailvalue= StringVar
passwordvalue= StringVar
paymentvalue= StringVar
checkvalue= IntVar


#Text field for entering data
nameentry=Entry(root,textvariable=namevalue).grid(row=2,column=3)
genderentry=Entry(root,textvariable=gendervalue).grid(row=4,column=3)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=6,column=3)
emailentry=Entry(root,textvariable=emailvalue).grid(row=8,column=3)
passwordentry=Entry(root,textvariable=passwordvalue , show="*").grid(row=10,column=3)
paymententry=Entry(root,textvariable=paymentvalue).grid(row=12,column=3)

# checkbox
checkbtn=Checkbutton(text="remember me" , variable=checkvalue).grid(row=14,column=3)


#submit button

Button(text="Submit",command=getvals).grid(row=16,column=3)

root.mainloop()