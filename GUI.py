from tkinter import *

window = Tk()
window.title("Добро пожаловать")
window.mainloop()
lbl = Label(window, text="Welcome")
#comments lbl , с помощью класса Label
lbl.grid(column=0, row=1)
window.mainloop()
#наброски графического интерфейса вернусь сюда после изучения класса и функций