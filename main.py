import tkinter

window=tkinter.Tk()
window.title("my first Gui")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
#label

my_label=tkinter.Label(text="label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

my_label["text"]="New Text"


def button_clidked():
    my_label["text"] = input.get()

button=tkinter.Button(text="click", command=button_clidked)
button.grid(column=1,row=1)
button2=tkinter.Button(text="click", command=button_clidked)
button2.grid(column=2,row=0)

input=tkinter.Entry(width=10)
input.grid(column=4,row=2)
window.mainloop()