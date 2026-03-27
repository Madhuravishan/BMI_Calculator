from tkinter import*
from tkinter import messagebox
def findbmi ():
    try:
        h=float(entrh.get())
        w=float(entrw.get())
        h=h/100
        bmi=w/(h*h)
        txtbmi.delete(0.0,"end")
        txta.delete(0.0,"end")
        txtbmi.insert(END,round(bmi,1))   
        if bmi<17: 
         txta.insert(END,"Get foods")
        elif  bmi>25:
         txta.insert(END,"No more foods")
        else:
         txta.insert(END,"You are healthy")   
    except:
         messagebox.showerror("InpuT Data error","Please fill weight and height")
def clear():
    entrh.delete(0,END)
    entrw.delete(0,END)
    txtbmi.delete(0.0,"end")
    txta.delete(0.0,"end")

win=Tk()
win.title('Find your BMI')
win.geometry('600x400')
win.configure(bg="black")
win.resizable(0,0)
win.columnconfigure(0,weight=2)
win.columnconfigure(1,weight=1)
Label(win,text="Calculate your Body Mass Index",\
           font="none 20",bg="#005500",fg="white")\
      .grid(row=0,column=0,columnspan=2,padx=10, pady=10)

lblh=Label(win,text="Enter your Height in cms:",font="none 15",bg="#005456",fg="white")
lblh.grid(row=1,column=0,sticky=W,padx=10, pady=10)
lblw=Label(win,text="Enter your Weight in kgs:",font="none 15",bg="#005456",fg="white")
lblw.grid(row=2,column=0,sticky=W,padx=10, pady=10)
lblbmi=Label(win,text="Your BMI:",font="none 15",bg="#005456",fg="white")
lblbmi.grid(row=3,column=0,sticky=W,padx=10, pady=10)
lbla=Label(win,text="Advice:",font="none 15",bg="#008563",fg="white")
lbla.grid(row=6,column=0,sticky=W,padx=10, pady=10)



entrh=Entry(win,font="none 13",width=10)
entrh.grid(row=1,column=1,padx=10,pady=10,sticky=W)
entrw=Entry(win,font="none 13",width=10)
entrw.grid(row=2,column=1,padx=10,pady=10,sticky=W)

txtbmi=Text(win,font="none 15",width=10,height=1)
txtbmi.grid(row=3,column=1,padx=10,pady=10,sticky=W)
txta=Text(win,font="none 15",width=25,height=1)
txta.grid(row=6,column=1,padx=10,pady=10,sticky=W)

btncal=Button(win,text="calculate",font="none 15",bg="cadet blue",width=10,command=findbmi)
btncal.grid(row=4,column=0,padx=10,pady=10)
btnclr=Button(win,text="clear",font="none 15",bg="cadet blue",width=10,command=clear)
btnclr.grid(row=4,column=1,padx=10,pady=1,sticky=W)


win.mainloop()


