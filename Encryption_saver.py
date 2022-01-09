import tkinter as tk

HEIGHT = 500
WIDTH = 500

def encryption(entry, entry1):
    entry1 = list(entry1)
    encrypt = entry + ' '
    for ent in entry1:
        asci = ord(ent)
        asci -= 10
        asci = chr(asci)
        encrypt = encrypt + asci

    f = open("Encryption.txt", "a")
    f.write(encrypt)
    f.write("\n")
    f.close()

def decryption(entry):
    a = ''
    f = open("Encryption.txt", "r")
    for idx, line in enumerate(f):
        a += line
        a = a.split()
        if a[0] == entry:
            break
        a = ''
    f.close()

    b = ''

    for i in range(1, len(a)):
        b = b + ' ' + a[i]

    encrypt = ''

    for ent in b:
        asci = ord(ent)
        asci += 10
        asci = chr(asci)
        encrypt = encrypt + asci

    entry3['text'] = encrypt[1:]


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


label = tk.Label(root, text="PASSWORD SAVER", bg='green')
label.place(relx=0.3, rely=0, relwidth=0.4, relheight=.1)

label1 = tk.Label(root, text="Enter name", bg='yellow')
label1.place(relx=0.05, rely=.15, relwidth=0.2, relheight=.05)

entry = tk.Entry(root)
entry.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

label2 = tk.Label(root, text="Enter Password", bg='yellow')
label2.place(relx=0.55, rely=.15, relwidth=0.2, relheight=.05)

entry1 = tk.Entry(root)
entry1.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

button = tk.Button(root, text="Encrypt", bg='red', font=41, command=lambda: encryption(entry.get(), entry1.get()))
button.place(relx=.35, rely=.35, relwidth=0.3, relheight=0.1)

label2 = tk.Label(root, text="Enter name", bg='yellow')
label2.place(relx=0.05, rely=.6, relwidth=0.2, relheight=.05)

entry2 = tk.Entry(root)
entry2.place(relx=0.05, rely=0.65, relwidth=0.4, relheight=0.1)

entry3 = tk.Label(root)
entry3.place(relx=0.55, rely=0.65, relwidth=0.4, relheight=0.1)


button = tk.Button(root, text="Decrypt", bg='red', font=41, command=lambda: decryption(entry2.get()))
button.place(relx=.35, rely=.8, relwidth=0.3, relheight=0.1)




root.mainloop()


