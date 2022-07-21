from tkinter import *

window = Tk() # Создаём объект класса Tk()

window.title('Первое графическое приложение') # Меняем название приложения
window.iconbitmap('img/python-for-all.ico') # Меняем логотип приложения
window.geometry('600x400+700+400') # Размеры и начальное расположение приложения
window.resizable(False, False) # Фиксируем размеры приложения
window.config(bg='grey') # Меняем цвет фона приложения

window.mainloop()