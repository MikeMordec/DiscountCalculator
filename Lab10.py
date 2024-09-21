'''
Created on May 4, 2022

@author: michaelmordec
'''

from tkinter import *
from tkinter.messagebox import *

def isValid():
    if(price.get()<0):
        showerror("ERROR", "Price should not be less than 0")
        return False
    if(discountPercentage.get()==5 and price.get()>15):
        showerror("ERROR", "Price should be in the range $0-$15")
        return False
    if(discountPercentage.get()==10 and (price.get()<15 or price.get()>35)):
        showerror("ERROR", "Price should be in the range $15-$35")
        return False
    if(discountPercentage.get()==20 and (price.get()<=35)):
        showerror("ERROR", "Price should be greater than $35")
        return False  
    return True

def calc():
    if(isValid()):
        d=price.get()*(discountPercentage.get()/100.0)
        new_price=price.get()-d
        t=0.08*(new_price)
        tft=new_price+t
        Label(text=f"Total after tax= $%.2f"%(tft)).grid(row=1,column=1)
        Label(text=f"Tax= $%.2f"%(t)).grid(row=1,column=2)
        Label(text=f"Discount= $%.2f"%(d)).grid(row=1,column=3)


rootWindow=Tk()
rootWindow.geometry("700x300")
discountPercentage=IntVar()
price=IntVar()

radioButton1 = Radiobutton(rootWindow, text="5%", variable=discountPercentage, value=5).grid(row=0, column=0)
radioButton2 = Radiobutton(rootWindow, text="10%", variable=discountPercentage, value=10).grid(row=1, column=0)
radioButton3 = Radiobutton(rootWindow, text="20%", variable=discountPercentage, value=20).grid(row=2, column=0)

inputLabel=Label(text="Input")
inputLabel.grid(row=0,column=1)

priceField=Entry(textvariable=price).grid(row=0,column=2)
totalButton = Button(rootWindow, text='Total', width=10, command=calc).grid(row=3, column=0)
exitButton = Button(rootWindow, text='Exit', width=10, command=rootWindow.destroy).grid(row=3, column=1)

rootWindow.mainloop()
    