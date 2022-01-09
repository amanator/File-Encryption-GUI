f = open("grt.txt", "a")
for i in range(2):
    write = input()
    f.write(write)
    f.write("\n")
f.close()

# import tkinter as tk
#
# HEIGHT = 500
# WIDTH = 500
#
# def encryption(entry, entry1):
#     entry1 = list(entry1)
#     encrypt = entry + ' '
#     for ent in entry1:
#         asci = ord(ent)
#         asci -= 10
#         asci = chr(asci)
#         encrypt = encrypt + asci
#
#     f = open("Encryption.txt", "a")
#     f.write(encrypt)
#     f.write("\n")
#     f.close()
#
# def decryption(entry):
#     entry = list(entry)
#     encrypt = ''
#     for ent in entry:
#         asci = ord(ent)
#         asci += 10
#         asci = chr(asci)
#         encrypt = encrypt + asci
#     label1['text'] = encrypt
#
#
# root = tk.Tk()
#
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#80c1ff')
# canvas.pack()
#
#
#
# label = tk.Label(root, text="PASSWORD SAVER", bg='blue')
# label.place(relx=0.3, rely=0, relwidth=0.4, relheight=.1)
#
# entry = tk.Entry(root)
# entry.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)
#
# entry1 = tk.Entry(root)
# entry1.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)
#
# button = tk.Button(root, text="Encrypt", bg='red', font=41, command=lambda: encryption(entry.get(), entry1.get()))
# button.place(relx=.35, rely=.35, relwidth=0.3, relheight=0.1)
#
# entry2 = tk.Entry(root)
# entry2.place(relx=0.05, rely=0.65, relwidth=0.4, relheight=0.1)
#
# entry3 = tk.Label(root)
# entry3.place(relx=0.55, rely=0.65, relwidth=0.4, relheight=0.1)
#
#
# button = tk.Button(root, text="Decrypt", bg='red', font=41, command=lambda: (entry.get()))
# button.place(relx=.35, rely=.8, relwidth=0.3, relheight=0.1)
#
#
#
#
# root.mainloop()


