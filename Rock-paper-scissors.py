from tkinter import *
from random import *

root = Tk()
root.title('Добро пожаловать в игру Камень ножницы бумага')
root.geometry('800x400')
root.resizable(width=False, height=False) #  для постоянства окна
root['bg'] = 'blue'

def play_game(player_choice): # функция определяющая выбор пользователя , ответ компьютера рандомный
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = choice(choices)
    labelText.configure(text=f'Вы выбрали: {player_choice}, Компьютер выбрал: {computer_choice}')
    if player_choice == computer_choice:
        resultText.configure(text='Ничья!')
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
         (player_choice == 'ножницы' and computer_choice == 'бумага') or \
         (player_choice == 'бумага' and computer_choice == 'камень'):
        resultText.configure(text='Вы выиграли!')
    else:
        resultText.configure(text='Компьютер выиграл!')

labelText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='red')
labelText.place(y=100, x=100)
resultText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='green')
resultText.place(y=150, x=100)
# кнопки камень ,бумага, ножницы:
stone = Button(root,
               text='Камень',
               font=('Comic Sans MS', 20),
               bg='white',
               command=lambda: play_game('камень'))

stone.place(x=50, y=300)

paper = Button(root,
               text='Бумага',
               font=('Comic Sans MS', 20),
               bg='white',
               command=lambda: play_game('бумага'))

paper.place(x=220, y=300)

scissors = Button(root,
               text='Ножницы',
               font=('Comic Sans MS', 20),
               bg='white',
               command=lambda: play_game('ножницы'))

scissors.place(x=420, y=300)
root.mainloop()