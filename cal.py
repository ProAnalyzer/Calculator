from tkinter import *

def btnclk(num):
 global op
 op=op+str(num)
 inp.set(op)
 
def clr():
 global op
 x=len(op)
 op=op[0:x-1]
 inp.set(op)
 
def clsr():
 global op
 op=""
 inp.set("")
 
def eql():
 global op
 if(op==""):
  inp.set("0")
 else:
  res=str(eval(op))
  inp.set(res)
  op=res
 
cal = Tk()
cal.title("Calculator")
op=""
inp=StringVar()
###########################################################################################
dispbox=Entry(cal,font=('arial',20),textvariable=inp,bd=7,insertwidth=7,
bg="wheat1",justify="right").grid(columnspan=4,ipady=10)
###########################################################################################
btn7=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="7",command=lambda:btnclk(7)).grid(row=1,column=0)
btn8=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="8",command=lambda:btnclk(8)).grid(row=1,column=1)
btn9=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="9",command=lambda:btnclk(9)).grid(row=1,column=2)
btnadd=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="+",command=lambda:btnclk("+")).grid(row=1,column=3)
###########################################################################################
btn4=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="4",command=lambda:btnclk(4)).grid(row=2,column=0)
btn5=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="5",command=lambda:btnclk(5)).grid(row=2,column=1)
btn6=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="6",command=lambda:btnclk(6)).grid(row=2,column=2)
btnsub=Button(cal,padx=26,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="-",command=lambda:btnclk("-")).grid(row=2,column=3)
###########################################################################################
btn1=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="1",command=lambda:btnclk(1)).grid(row=3,column=0)
btn2=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="2",command=lambda:btnclk(2)).grid(row=3,column=1)
btn3=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="3",command=lambda:btnclk(3)).grid(row=3,column=2)
btnmul=Button(cal,padx=25,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="*",command=lambda:btnclk("*")).grid(row=3,column=3)
###########################################################################################
btndbz=Button(cal,padx=16,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="00",command=lambda:btnclk("00")).grid(row=4,column=0)
btn0=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="snow1",font=('arial',16),
text="0",command=lambda:btnclk(0)).grid(row=4,column=1)
btndiv=Button(cal,padx=25,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="/",command=lambda:btnclk("/")).grid(row=4,column=2)
btnpow=Button(cal,padx=25,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="^",command=lambda:btnclk("**")).grid(row=4,column=3)
###########################################################################################
btnc=Button(cal,padx=21,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="C",command=clr).grid(row=5,column=0)
btnmod=Button(cal,padx=15,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text="CE",command=clsr).grid(row=5,column=1)
btndot=Button(cal,padx=25,pady=10,bd=4,fg="black",bg="snow3",font=('arial',16),
text=".",command=lambda:btnclk(".")).grid(row=5,column=2)
btneql=Button(cal,padx=23,pady=10,bd=4,fg="black",bg="orange red",font=('arial',16),
text="=",command=eql).grid(row=5,column=3)
############################################################################################
cal.mainloop()

#In E:/Scripts 
#pip install pyinstaller
#pyinstaller -w -i <icon location> --onefile cal.py