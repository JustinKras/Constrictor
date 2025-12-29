import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sys
import os

from pynput.mouse import Listener
from pynput import keyboard
import threading
import mouse
import win32api
import time
import random
import string

import ctypes
from ctypes import wintypes


SECRET_PASSWORD = "letmein"
KILL_SWITCH = "<Control-Shift-X>"


#subprocess.Popen(["k_l_.exe"])

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def random_title(length=99):
    return ''.join(random.choices(string.ascii_letters, k=length))

def do_nothing():
    messagebox.showerror("Notice", "You cannot close this window!\nEnter the password to exit.")

def check_password(event=None):
    if password_entry.get() == SECRET_PASSWORD:
        root.destroy()
        process_name = "k_l_.exe"
        subprocess.run(["taskkill", "/f", "/im", process_name], shell=True)

    else:
        messagebox.showwarning("Incorrect", "Wrong password! Try again.")
        password_entry.delete(0, tk.END)

def kill_switch(event=None):
    root.destroy()
    process_name = "k_l_.exe"
    subprocess.run(["taskkill", "/f", "/im", process_name], shell=True)



root = tk.Tk()
root.title(random_title())
root.protocol("WM_DELETE_WINDOW", do_nothing)
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.config(cursor="none")
root.configure(bg="black")

'''logo_image = Image.open("lock.png")
img_path = resource_path("lock.png")
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="black")
logo_label.pack(pady=20)'''

########

# open image using bundled-safe path
img_path = resource_path("lock.png")
logo_image = Image.open(img_path)

# resize AFTER opening
logo_image = logo_image.resize((200, 200), Image.LANCZOS)

# convert for Tkinter
logo_photo = ImageTk.PhotoImage(logo_image)

# keep reference or Tkinter will garbage collect it
logo_label = tk.Label(root, image=logo_photo, bg="black")
logo_label.image = logo_photo
logo_label.pack(pady=20)

########

label = tk.Label(root, text="This Device Is Now Locked", font=("Ariel", 24), fg="white", bg="black")
label.pack(expand=False)

label = tk.Label(root, text="This window cannot be closed normally!", font=("Ariel", 20), fg="white", bg="black")
label.pack(pady=2)

instr_label = tk.Label(root, text="Type the password below and press enter", font=("Arial", 16), fg="white", bg="black")
instr_label.pack(pady=10)

label = tk.Label(root, text="Passkey - letmein", font=("Ariel", 20, "bold"), fg="white", bg="black")
label.pack(pady=5)

label = tk.Label(root, text="© 2026 JustinKras. All Rights Reserved. Unauthorized Access Prohibited.", font=("Ariel", 11), fg="white", bg="black")
label.pack(pady=20)
label.place(x=0, y=1030)
                 

password_entry = tk.Entry(root, show="*", font=("Arial", 16))
password_entry.pack(pady=10)
password_entry.focus_set()
password_entry.config(cursor="none")

password_entry.bind("<Return>", check_password)

root.bind(KILL_SWITCH, kill_switch)

root.iconbitmap(resource_path("icon.ico"))

root.mainloop()
