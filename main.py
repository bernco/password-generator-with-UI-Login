from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_details():
    web = website_entry.get()
    try:
        with open("data.json", 'r') as file:
            # read file
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="Your password manager is empty")

    else:
        if web in data:
            e_mail = data[web]["email"]
            pass_wd = data[web]["password"]
            messagebox.showinfo(title=f"{web}", message=f"Your details are:\nPassword: {pass_wd}\n"
                                                        f"Email: {e_mail}")
        else:
            messagebox.showerror(title="Oops", message=f"Your {web} details was not found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    web = website_entry.get()
    e_mail = email_entry.get()
    pass_w = password_entry.get()
    new_data_dict = {
        web: {
            "email": e_mail,
            "password": pass_w
        }
    }
    if len(web) == 0 or len(e_mail) == 0 or len(pass_w) == 0:
        messagebox.showerror(title="Oops", message="Please ensure that no field is left blank")
    else:
        # open file
        try:
            with open("data.json", 'r') as file:
                # read file
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                # write file
                json.dump(new_data_dict, file, indent=4)
        else:
            # update data
            data.update(new_data_dict)
            with open("data.json", 'w') as file:
                # write file
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


# canvas
canvas = Canvas(width=100, height=160)
image = PhotoImage(file="logo.png")
canvas.create_image(50, 80, image=image)
canvas.grid(column=2, row=1)

# labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# entries
website_entry = Entry(width=18)
website_entry.grid(column=2, row=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "bernco@email.com")

password_entry = Entry(width=18)
password_entry.grid(column=2, row=4)

# button
generate_button = Button(text="Generate Password", command=password_gen)
generate_button.grid(column=3, row=4, )

add_button = Button(text="Add", width=30, command=add_data)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", width=14, command=search_details)
search_button.grid(column=3, row=2)

window.mainloop()
