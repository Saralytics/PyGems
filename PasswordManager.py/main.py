from tkinter import *
from tkinter import messagebox
from utils.password_generator import PasswordGenerator
import pyperclip
from utils.helper import Helper

LOGO_PATH = "logo.png"
DATA_PATH = "data.json"
pg = PasswordGenerator()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_and_populate():
    new_password = pg.generate()
    print(new_password)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


def search():
    try:
        searcher = Helper(website_entry, DATA_PATH)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Data file not found")
    else:
        try:
            if searcher.search():
                search_term, email, pwd = searcher.search()
                messagebox.showinfo(title=f"{search_term}", message=f"{search_term}: email {email}, password {pwd}")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="You have no data yet, please add some first")
        else:
            messagebox.showinfo(title="Error", message="No entry found")
    finally:
        website_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website: str = website_entry.get()
    email: str = email_entry.get()
    password: str = password_entry.get()
    new_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you didn't leave any field empty")
    else:
        try:
            saver = Helper(website_entry, DATA_PATH)
            saver.save(new_entry)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Your new website and password is saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=23)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "zhaoxue.li@alumni.ie.edu")
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate", width=8, command=generate_and_populate)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=8, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
