from tkinter import *

window = Tk() # Создаём объект класса Tk()

window.title('Первое графическое приложение') # Меняем название приложения
window.iconbitmap('img/python-for-all.ico') # Меняем логотип приложения
window.geometry('600x400+700+400') # Размеры и начальное расположение приложения
window.resizable(False, False) # Фиксируем размеры приложения
window.config(bg='grey') # Меняем цвет фона приложения

def hello():
	print('Привет!')

# button_1 = Button(window, text = 'Кнопка 1', command = hello, width = 10, height = 2, bd = 10, font = 'Arial 10 bold')
button_1 = Button(window, text = 'Кнопка 1', padx = 5, pady = 5, bd = 10, activebackground = 'yellow', activeforeground = 'orange', bg = 'green', fg = 'white')

button_1.pack()

window.mainloop()