import tkinter as tk


class MyButton(tk.Button):

    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = 0
        self.is_mine = False
        self.count_bombs = 0
        self.opened = False
        self.flag = False

    # Функция для расстановки флажка
    def set_flag(self, event):
        if self.opened is False:
            if self.flag is False:
                self.config(text='F', background="#c44da4")
                self.flag = True
            else:
                self.config(text='', background="white")
                self.flag = False
