import tkinter as tk
from random import shuffle
from MyButton import MyButton

colors = {
    1: '#2976f2',
    2: '#25c47d',
    3: '#dba91f',
    4: '#8b0eb5',
    5: '#c9126b',
    6: '#06c0c9',
    7: '#bfc42d',
    8: '#c42727'}


class MineSweeper:
    window = tk
    winner = None
    looser = None

    def __init__(self, mines, width, height):
        self.window = tk.Tk()
        self.window.title('MineSweeper')
        self.mines = mines
        self.height = height
        self.width = width
        self.buttons = []
        for i in range(self.height):
            temp = []
            for j in range(self.width):
                self.button = MyButton(self.window, x=i, y=j, width=3, font="Calibre 15 bold",
                                       background="white")
                self.button.config(command=lambda button=self.button: self.click(button))
                temp.append(self.button)
            self.buttons.append(temp)

    # Запуск игры
    def start(self):
        self.create_field()
        self.get_mines_nums()
        self.set_mines()
        self.count_mines()
        self.print_buttons()
        MineSweeper.window.mainloop()

    # Создание поля
    def create_field(self):
        for i in range(self.height):
            for j in range(self.width):
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].bind('<Button-3>', self.buttons[i][j].set_flag)

    # Проверка, открыто ли все поле
    def check_field(self):
        for i in range(self.height):
            for j in range(self.width):
                button = self.buttons[i][j]
                if button.is_mine is False and button.opened is False:
                    return
        self.win()

    # Вывод поля в консоль
    def print_buttons(self):
        for i in range(self.height):
            for j in range(self.width):
                button = self.buttons[i][j]
                if button.is_mine:
                    print("B", end='')
                else:
                    print(button.count_bombs, end='')
            print()

    # Открытие всех кнопок (в случае поражения)
    def open_all_buttons(self):
        for i in range(self.height):
            for j in range(self.width):
                button = self.buttons[i][j]
                if button.is_mine:
                    button.config(text="*", background="red", disabledforeground="black")
                else:
                    color = colors.get(button.count_bombs, "black")
                    button.config(text=button.count_bombs, disabledforeground=color)
                button.config(state="disabled")

    # Функция для определения номеров бомб
    def get_mines_nums(self):
        nums = list(range(1, self.width * self.height + 1))
        shuffle(nums)
        return nums[:self.mines]

    # Функция для расстановки бомб
    def set_mines(self):
        nums = self.get_mines_nums()
        count = 1
        for i in range(self.height):
            for j in range(self.width):
                button = self.buttons[i][j]
                button.number = count
                if button.number in nums:
                    button.is_mine = True
                count += 1

    # Обработка клика левой кнопкой мыши
    def click(self, clicked_button):
        print(clicked_button)
        clicked_button.opened = True
        if clicked_button.is_mine:
            self.open_all_buttons()
            self.lose()
            return
        color = colors.get(clicked_button.count_bombs, "black")
        clicked_button.config(text=clicked_button.count_bombs, disabledforeground=color, background='white')
        if clicked_button.count_bombs is 0:
            self.open_neighbours(clicked_button.x, clicked_button.y)
        clicked_button.config(state="disabled")
        self.check_field()

    # Функция для открытия соседей (если вокруг клетки нет мин)
    def open_neighbours(self, i, j):
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if i + x < 0 or j + y < 0 or i + x >= self.height or j + y >= self.width:
                    continue
                button = self.buttons[i + x][j + y]
                if button.opened is True:
                    continue
                button.opened = True
                color = colors.get(button.count_bombs, "black")
                button.config(text=button.count_bombs, disabledforeground=color, background='white')
                if button.count_bombs is 0:
                    self.open_neighbours(i + x, j + y)
                button.config(state="disabled")

    # Функция для подсчета мин вокруг каждой клетки
    def count_mines(self):
        for i in range(self.height):
            for j in range(self.width):
                button = self.buttons[i][j]
                count = 0
                if not button.is_mine:
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if i + x < 0 or j + y < 0 or i + x >= self.height or j + y >= self.width:
                                continue
                            neighbour = self.buttons[i + x][j + y]
                            if neighbour.is_mine is True:
                                count += 1
                button.count_bombs = count

    # Сообщение о выигрыше
    def win(self):
        self.winner = tk.Tk()
        self.winner.title('Congratulations!')
        self.winner.geometry('300x150')
        text = tk.Label(self.winner, font="14", text='You won!!!')
        button = tk.Button(self.winner, text='OK :)', command=self.close_window)
        text.place(x=100, y=40)
        button.place(x=130, y=90)
        self.winner.mainloop()

    # Сообщение о проигрыше
    def lose(self):
        self.looser = tk.Tk()
        self.looser.title('Oh, we are very sorry...')
        self.looser.geometry('300x150')
        text = tk.Label(self.looser, font="14", text='You lose...')
        button = tk.Button(self.looser, text='I will try again :)', command=self.close_window)
        text.place(x=100, y=40)
        button.place(x=100, y=90)
        self.looser.mainloop()

    # Закрытие окон
    def close_window(self):
        if self.looser is None:
            self.winner.destroy()
        else:
            self.looser.destroy()
        self.window.destroy()
