import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == '0':
        display_var.set(symbol)
    else:
        display_var.set(current + symbol)

def clear_display():
    display_var.set('0')

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

# Ana uygulama penceresi
root = tk.Tk()
root.title("Hesap Makinesi")

# Ekran için değişken
display_var = tk.StringVar()
display_var.set('0')

# Ekran widget'ı
display = tk.Entry(root, textvariable=display_var, justify='right', font=('Arial', 14))
display.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Butonlar
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, command=calculate, font=('Arial', 14), padx=20)
    elif text == 'C':
        btn = tk.Button(root, text=text, command=clear_display, font=('Arial', 14), padx=20)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: button_click(t), font=('Arial', 14))
    btn.grid(row=row, column=col, sticky='nsew')

# Butonların grid konfigürasyonu
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
