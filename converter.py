from tkinter import *
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=110,height=110)
window.config(padx=20,pady=20)

input=Entry()
input.grid(column=1, row=0)

text1=Label(text="Miles")
text1.grid(column=2, row=0)

text2=Label(text="is equal to")
text2.grid(column=0, row=1)

text3=Label(text=0)
text3.grid(column=1, row=1)

text4=Label(text="Km")
text4.grid(column=2, row=1)
def convert():
    text3["text"]=round(float(input.get())*1.609,2)

button=Button(text="Calculate",command=convert)
button.grid(column=1, row=2)



window.mainloop()