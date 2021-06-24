import tkinter as tk
from tkinter import END
from MineSweeper import MineSweeper


# Обработка пользовательских данных и создание игры
def create_with_params():
    if mine_text.get('1.0', END) is not "\n":
        mines = int(mine_text.get('1.0', END))
    else:
        mines = 5
    if width_text.get('1.0', END) is not "\n":
        width = int(width_text.get('1.0', END))
    else:
        width = 10
    if height_text.get('1.0', END) is not "\n":
        height = int(height_text.get('1.0', END))
    else:
        height = 10

    settings.destroy()
    game = MineSweeper(mines, width, height)
    game.start()


# Создания окна с настройками
settings = tk.Tk()
settings.title('Settings')
settings.geometry('300x150')
mine_text = tk.Text(settings, width=5, height=1)
mine_label = tk.Label(settings, height=1, text='Bombs:')
width_text = tk.Text(settings, width=5, height=1)
width_label = tk.Label(settings, height=1, text='Width:')
height_text = tk.Text(settings, width=5, height=1)
height_label = tk.Label(settings, height=1, text='Height:')
button = tk.Button(settings, text='Start', command=create_with_params)
button.place(x=130, y=100)
mine_text.place(x=160, y=15)
mine_label.place(x=90, y=15)
width_text.place(x=160, y=40)
width_label.place(x=90, y=40)
height_text.place(x=160, y=65)
height_label.place(x=90, y=65)
settings.mainloop()
