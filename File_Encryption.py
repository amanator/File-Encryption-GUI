import tkinter as tk
import pathlib

HEIGHT = 500
WIDTH = 500


def encryption(entry, entry1):
    path = pathlib.Path(entry)
    file_path = path / entry1
    f = open(file_path, "rt")
    string = list(f.read())
    encrypt = ''

    for lines in string:
        if lines == "\t":
            lines = 'a'
        ascii = ord(lines)
        ascii -= 10
        ascii = chr(ascii)
        encrypt = encrypt + ascii

    f.close()

    f = open(file_path, "wt")
    f.write(encrypt)
    f.close()


def decryption(entry, entry1):
    path = pathlib.Path(entry)
    file_path = path / entry1
    f = open(file_path, "rt")
    string = list(f.read())
    encrypt = ''

    for lines in string:
        if lines == "\t":
            lines = 'a'
        ascii = ord(lines)
        ascii += 10
        ascii = chr(ascii)
        encrypt = encrypt + ascii

    f.close()

    f = open(file_path, "wt")
    f.write(encrypt)
    f.close()


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()  



label = tk.Label(root, text="PASSWORD SAVER", bg='blue')
label.place(relx=0.3, rely=0, relwidth=0.4, relheight=.1)

label1 = tk.Label(root, text="Enter file path", bg='yellow')
label1.place(relx=0.05, rely=0.35, relwidth=0.4, relheight=.05)

entry = tk.Entry(root)
entry.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)

label2 = tk.Label(root, text="Enter file name with extention", bg='yellow')
label2.place(relx=0.55, rely=0.35, relwidth=0.4, relheight=.05)

entry1 = tk.Entry(root)
entry1.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

button = tk.Button(root, text="Encrypt File", bg='red', font=41, command=lambda: encryption(entry.get(), entry1.get()))
button.place(relx=.35, rely=.55, relwidth=0.3, relheight=0.1)

button = tk.Button(root, text="Decrypt File", bg='red', font=40, command=lambda: decryption(entry.get(), entry1.get()))
button.place(relx=.35, rely=.7, relwidth=0.3, relheight=0.1)





root.mainloop()
