from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def automatic_generate():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    for i in range(nr_letters):
        password_list.append(random.choice(letters))
    for i in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for i in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    final_string = "".join(password_list)
    password_entry.insert(END, string=final_string)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.minsize(600, 600)
screen.config(bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0,bg="white")
image1 = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=image1)
canvas.place(x=205, y= 30)

my_name = Label(text="By Arsh", font=("Ariel", 15, "italic bold"), bg="#FF7F24", fg="#1874CD")
my_name.place(x=265, y = 230)

website_label = Label(text="Website:",font=("Ariel", 12, "bold"), bg="#DEB887")
website_label.place(x = 40, y=300)

website_entry = Entry(width=25, bg="#f7f5dd", font=("Ariel", 15))
website_entry.place(x=123,y=299)
website_entry.focus()

email_label = Label(text="Email/Username:",font=("Ariel", 12, "bold"), bg="#DEB887")
email_label.place(x=10, y=350)

email_entry = Entry(width=30, bg="#f7f5dd", font=("Ariel", 15))
email_entry.place(x= 180, y= 349)
email_entry.insert(0, string="arshsharma901@gmail.com")

password_label = Label(text="Password:",font=("Ariel", 12, "bold"), bg="#DEB887")
password_label.place(x=30, y= 400)

password_entry = Entry(width=27, bg="#f7f5dd", font=("Ariel", 12))
password_entry.place(x=150, y=401)

password_generate_button = Button(text="Generate Password", font=("Ariel", 10), command=automatic_generate)
password_generate_button.place(x= 430, y=395)

def addition():
    if len(website_entry.get()) != 0 and len(email_entry.get()) != 0 and len(password_entry.get()) != 0:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Details entered:\nWebsite: {website_entry.get()}\nUsername/Email: {email_entry.get()}\nPassword: {password_entry.get()}")
        if is_ok:
            cred = {website_entry.get():{"email":email_entry.get(), "password":password_entry.get()}}
            try:
                with open("list.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(cred)
            except FileNotFoundError:
                with open("list.json", "w") as data_file:
                    json.dump(cred, data_file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("list.json", "w") as data_file:
                    json.dump(cred, data_file, indent=4)
            else:
                with open("list.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
    else:
        messagebox.showerror(title="Warning", message="You seem to have left out some of the details. Please fill all the information to continue.")

add_button = Button(text="Add!", font=("Ariel", 15, "bold"), command=addition)
add_button.place(x=270, y=450)

def search():
    try:
        with open("list.json", "r") as file:
            data1 = json.load(file)
            if website_entry.get() in data1.keys():
                messagebox.showinfo(title=f"{website_entry.get()}", message=f"Website: {website_entry.get()}\nUsername/Email: {data1[website_entry.get()]['email']}\nPassword: {data1[website_entry.get()]['password']}")

            else:
                messagebox.showerror(title=f"{website_entry.get()}", message="The website you entered has not been stored in the database. You need to add it first.")
    except json.decoder.JSONDecodeError:
        with open("list.json", "w") as file:
            file.write("{}")
            data1 = son.load(file)
            if website_entry.get() in data1.keys():
                messagebox.showinfo(title=f"{website_entry.get()}", message=f"Website: {website_entry.get()}\nUsername/Email: {data1[website_entry.get()]['email']}\nPassword: {data1[website_entry.get()]['password']}")

            else:
                messagebox.showerror(title=f"{website_entry.get()}", message="The website you entered has not been stored in the database. You need to add it first.")


search_button = Button(text="Search", font=("Ariel", 12), command=search)
search_button.place(x=460, y=295)

screen.mainloop()
