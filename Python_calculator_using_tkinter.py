# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 02:41:42 2022

@author: Lenovo
"""
from tkinter import *
cal=Tk()
cal.title("DETAILS")
cal.minsize(410,400)

def per():  
    maths=ma.get()
    chem=che.get()
    phys=phy.get()
    engli=eng.get()
    compu=comp.get()
    add=int(maths)+int(chem)+int(phys)+int(engli)+int(compu)
    add1=add*100
    fper=add1/500
    result="PERCENTAGE ="+str(fper)+"%"
    label.config(text=result)
def show():
    
    ide=sap.get()
    n=fna.get()+lna.get()
    l="DETAILS\n"
    f=l+"NAME  -" +str(n)+"\n"
    det=f+"SAP ID-"+str(ide)
    label2.config(text=det)
    
    
fna=StringVar()
lna=StringVar()
sap=StringVar()
ma=StringVar()
phy=StringVar()
che=StringVar()
eng=StringVar()
comp=StringVar()
l1=Label(cal,text="STUDENT PERCENTAGE CALCULATOR",font=('Helvetica', 12, 'bold'),fg="Red").place(x=30,y=40)
l2=Label(cal,text="FIRST NAME").place(x=20,y=70)
x2=Entry(cal,textvariable=fna).place(x=100,y=70)
l3=Label(cal,text="LAST NAME").place(x=20,y=90)
x3=Entry(cal,textvariable=lna).place(x=100,y=90)
l4=Label(cal,text="SAPID").place(x=20,y=110)
x4=Entry(cal,textvariable=sap).place(x=100,y=110)
l5=Label(cal,text="MARKS DETAIL",font=('Helvetica', 10, 'bold'),fg="Red").place(x=150,y=130)
l6=Label(cal,text="MATHS").place(x=20,y=150)
x6=Entry(cal,textvariable=ma).place(x=100,y=150)
l7=Label(cal,text="PHYSICS").place(x=20,y=170)
x7=Entry(cal,textvariable=phy).place(x=100,y=170)
l8=Label(cal,text="CHEMISTRY").place(x=20,y=190)
x8=Entry(cal,textvariable=che).place(x=100,y=190)
l9=Label(cal,text="ENGLISH").place(x=20,y=210)
x9=Entry(cal,textvariable=eng).place(x=100,y=210)
l10=Label(cal,text="COMPUTER").place(x=20,y=230)
x10=Entry(cal,textvariable=comp).place(x=100,y=230)
b1=Button(cal,text="CLICK HERE TO CALCULATE %",command=per,activebackground="red",activeforeground="black").place(x=20,y=250)
b2=Button(cal,text="SHOW DETAILS",command=show,activebackground="red",activeforeground="black").place(x=200,y=250)
label=Label(cal)
label.pack(side=BOTTOM)
label2=Label(cal)
label2.place(x=130,y=290)
cal.mainloop()
