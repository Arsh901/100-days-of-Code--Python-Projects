import tkinter
from tkinter import *

screen = Tk()
screen.minsize(500, 500)
screen.title("GUI Unit Converter!")
screen.config(bg="brown")
welcome_label = Label(text="Welcome to GUI Converter", font=("Times New Roman", 30, "bold"), bg="red")
welcome_label.place(x=15,y= 0)

my_name = Label(text="By Arsh", font=("Ariel", 20, "italic"), bg="yellow")
my_name.place(x=200, y=90)

input_entry = Entry(width=10, font=("Ariel 14 bold"))
input_entry.place(x=195,y=180)

km_label = Label(text="Km", font=("Ariel", 20, "bold"))
km_label.place(x=370, y=175)

converted_label = Label(text="0", font=("Ariel", 20, "bold"))
converted_label.place(x=245, y=230)

def calculate():
    val = float(input_entry.get())
    miles_value = val * 0.621
    converted_label["text"] = miles_value
    converted_label.place(x=215, y=230)

is_equal_label = Label(text="is equal to", font=("Ariel", 20))
is_equal_label.place(x=40, y=227)

miles_label = Label(text="miles", font=("Ariel", 20, "bold"))
miles_label.place(x=360, y=228)

calculate_button = Button(text="Calculate", font=("Ariel 15 bold"), command=calculate)
calculate_button.place(x=205, y=300)



screen.mainloop()