from tkinter import *
import math

def leftClickbutton(event):
    resule = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if resule >= 30:
        labelResult.configure(text=str(resule)+"อ้วนมาก")
    elif resule >= 25:
        labelResult.configure(text=str(resule)+"อ้วน")
    elif resule >= 23:
        labelResult.configure(text=str(resule)+"น้ำหนักเกิน")
    elif resule >= 18.6:
        labelResult.configure(text=str(resule)+"น้ำหนักปกติ")
    else:
        labelResult.configure(text=str(resule)+"ผอมเกินไป")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (Cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.bind("<Button-1>",leftClickbutton)
calculateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
mainWindow.mainloop()