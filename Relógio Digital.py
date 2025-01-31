import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Relógio Digital")

def relogio():
    hora = strftime('%H:%M:%S')
    label.config(text=hora)
    label.after(1000, relogio)

label = tk.Label(root, font=('Arial', 48),
background = 'black', foreground =  'white')

label.pack(anchor='center')


relogio()
root.mainloop()