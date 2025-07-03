import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(500,300)

label = tkinter.Label(text="Hi i am a label", font=("arial",30,"bold"))
label.pack()

def button_clicked():
     new_text = input.get()
     label.config(text=new_text)

dis_button = tkinter.Button(text="Click me" , command=button_clicked)
dis_button.pack()

input = tkinter.Entry()
input.pack()
#new line added
#yayy another line added

window.mainloop()