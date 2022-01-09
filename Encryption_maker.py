import tkinter as tk

HEIGHT = 500
WIDTH = 500

def encryption(entry):
    entry = list(entry)
    encrypt = ''
    for ent in entry:
        asci = ord(ent)
        asci -= 10
        asci = chr(asci)
        encrypt = encrypt + asci
    label1['text'] = encrypt


def decryption(entry):
    entry = list(entry)
    encrypt = ''
    for ent in entry:
        asci = ord(ent)
        asci += 10
        asci = chr(asci)
        encrypt = encrypt + asci

    label1['text'] = encrypt


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text="PASSWORD SAVER", bg='blue')
label.place(relx=0.3, rely=0, relwidth=0.4, relheight=.1)

entry = tk.Entry(frame)
entry.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)



button = tk.Button(frame, text="Encrypt", bg='red', font=41, command=lambda: encryption(entry.get()))
button.place(relx=.35, rely=.55, relwidth=0.3, relheight=0.1)

button = tk.Button(frame, text="Decrypt", bg='red', font=40, command=lambda: decryption(entry.get()))
button.place(relx=.35, rely=.7, relwidth=0.3, relheight=0.1)


label1 = tk.Label(frame)
label1.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

root.mainloop()
