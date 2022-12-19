import random
import tkinter
import string

# List of characters thar will be used to generate password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


# function to generate password
def generate_pass(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)


# CODE FOR GUI
#  In order to create a tkinter application,
# we generally create an instance of tkinter frame, 
# i.e., Tk(). It helps to display the root window and manages all the other components of the tkinter application
main_window = tkinter.Tk()
main_window.title("Pass Gen")
# window dimensions
main_window.geometry('300x300')
padd = 50
main_window['padx'] = padd

# Converting the length into an integer
len1 = tkinter.IntVar()
len2 = tkinter.IntVar()
len3 = tkinter.IntVar()


def get_length():
    if len1.get() == 8:
        generate_pass(8)
    elif len2.get() == 12:
        generate_pass(12)
    elif len3.get() == 16:
        generate_pass(16)
    else:
        generate_pass(0)


title_text = tkinter.Label(text='RANDOM PASSWORD GENERATOR')
title_text.grid(row=0, column=0)
# creating 3 rows 1st row will show password 2nd and 3rd row will have options for password length and in
# 4th row we will generate password button which will invoke our password function
display_result = tkinter.Entry()
display_result.grid(row=1, column=0)

check1 = tkinter.Checkbutton(text='8 Character', onvalue=8, offvalue=0, variable=len1)
check1.grid(row=3, column=0)
check2 = tkinter.Checkbutton(text='12 Character', onvalue=12, offvalue=0, variable=len2)
check2.grid(row=4, column=0)
check3 = tkinter.Checkbutton(text='16 Character', onvalue=16, offvalue=0, variable=len3)
check3.grid(row=5, column=0)

pass_generate = tkinter.Button(text='Generate', command=get_length)
pass_generate.grid(row=7, column=0)

# window.mainloop() tells Python to run the Tkinter event loop.
main_window.mainloop()
