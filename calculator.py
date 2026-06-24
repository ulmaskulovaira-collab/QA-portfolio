import tkinter as tk
from tkinter import font

# ---- Функция обработки нажатий (НЕ ТРОГАЕМ, всё работает) ----
def click(b):
    current = display.get()

    if b == 'C':
        display.delete(0, tk.END)
    elif b == '=':
        try:
            expr = current.replace('%', '/100')
            result = eval(expr)
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "ОШИБКА")
    elif b == '()':
        if current == '' or current[-1] in '+-*/(':
            display.insert(tk.END, '(')
        else:
            display.insert(tk.END, ')')
    elif b == '%':
        display.insert(tk.END, '/100')
    elif b == '+-':
        if current.startswith('-'):
            display.delete(0, 1)
        else:
            display.insert(0, '-')
    else:
        display.insert(tk.END, b)

# ---- Окно ----
root = tk.Tk()
root.title("КАЛЬКУЛЯТОР")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#fce4ec")  # Очень светлый розовый фон

# ---- Пиксельный шрифт (если нет Press Start 2P — используем Courier) ----
try:
    pixel_font = font.Font(family="Press Start 2P", size=12)
    pixel_font_big = font.Font(family="Press Start 2P", size=22)
except:
    pixel_font = font.Font(family="Courier", size=12, weight="bold")
    pixel_font_big = font.Font(family="Courier", size=22, weight="bold")

# ---- Экран (светлый, нежно-розовый текст) ----
display = tk.Entry(root, font=pixel_font_big, justify="right",
                   bd=5, relief="solid", bg="#ffffff", fg="#d81b60",
                   insertbackground="#d81b60", highlightthickness=2,
                   highlightcolor="#f48fb1")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

# ---- Все кнопки (полный набор) ----
buttons = [
    'C', '()', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+-', '0', '.', '='
]

# ---- Расставляем с нежно-розовыми цветами ----
row = 1
col = 0
for btn in buttons:
    # Определяем цвета для каждой группы
    if btn == '=':
        bg_color = "#ec407a"      # яркий, но нежный розовый
        fg_color = "white"
        active_bg = "#d81b60"
    elif btn == 'C':
        bg_color = "#ef5350"      # мягкий красный
        fg_color = "white"
        active_bg = "#c62828"
    elif btn in ('()', '%', '+-'):
        bg_color = "#f06292"      # средний розовый
        fg_color = "white"
        active_bg = "#d81b60"
    elif btn in ('/', '*', '-', '+'):
        bg_color = "#f48fb1"      # светлый розовый для операций
        fg_color = "#880e4f"
        active_bg = "#f06292"
    else:  # цифры и точка
        bg_color = "#f8bbd0"      # самый нежный розовый
        fg_color = "#880e4f"
        active_bg = "#f48fb1"

    button = tk.Button(root, text=btn, font=pixel_font,
                       width=4, height=2,
                       relief="raised", bd=3,           # пиксельная рамка
                       bg=bg_color, fg=fg_color,
                       activebackground=active_bg,
                       activeforeground="white" if btn in ('=', 'C', '()', '%', '+-') else "#880e4f",
                       highlightthickness=2,
                       highlightcolor="#f8bbd0")

    button.config(command=lambda b=btn: click(b))
    button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

# ---- Растягиваем строки и столбцы ----
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# ---- Запуск ----
root.mainloop()
