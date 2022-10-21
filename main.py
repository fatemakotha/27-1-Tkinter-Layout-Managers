#pack() place() and grid() : ******

from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

my_window = Tk()
my_window.title("My first GUI program")
my_window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# # my_label.pack() #or we can use place()
# my_label.place(x=0, y=0) #places my_label at the TOP LEFT CORNER
my_label.grid(column=0, row=0) #places my_label at the TOP LEFT CORNER
# my_label.grid(column=5, row=5) #STILL places my_label at the TOP LEFT CORNER because there is nothing in the prev ros and columns


#Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)






my_window.mainloop()