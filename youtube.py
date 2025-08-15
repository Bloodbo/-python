import threading
from tkinter import *
from tkinter import messagebox, filedialog
import pytube

# создаем главное окно
root = Tk()
root.title("Загрузка видео с YouTube")
root.geometry("600x400")
root.configure(bg='#D3D3D3')

# заголовок формы
lb = Label(root, text="Загрузка видео с YouTube", font=('Arial', 14, 'bold'), bg='#D3D3D3')
lb.pack(pady=15)

# пояснительный текст для поля с адресом
lb1 = Label(root, text="Ссылка на видео :", font=('Arial', 14, 'bold'), bg='#D3D3D3')
lb1.place(x=10, y=80)

# поле ввода адреса видео
link1 = StringVar()
En1 = Entry(root, textvariable=link1, font=('Arial', 14, 'bold'))
En1.place(x=230, y=80)

# функция скачивания
def download():
    # создаем поток для загрузки видео
    threading.Thread(target=download_thread).start()

def download_thread():
    try:
        # формируем адрес
        ytlink = link1.get()
        # переводим его в нужный формат
        youtubelink = pytube.YouTube(ytlink)
        # получаем ссылку на видео с самым высоким качеством
        video = youtubelink.streams.get_highest_resolution()
        # запрашиваем директорию для сохранения видео
        download_path = filedialog.askdirectory()
        if download_path:
            # скачиваем видео
            video.download(download_path)
            # выводим результат
            Result = "Загрузка завершена"
            messagebox.showinfo("Готово", Result)
        else:
            messagebox.showwarning("Предупреждение", "Вы не выбрали директорию для загрузки")
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror("Ошибка", "Недействительная ссылка")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# функция очистки
def reset():
    link1.set("")

# функция выхода
def Exit():
    root.destroy()

# кнопка скачивания
btn1 = Button(root, text="Скачать", font=('Arial', 9, 'bold'), bd=4, command=download)
btn1.place(x=330, y=130)

# кнопки очистки и выхода
btn2 = Button(root, text="Очистить", font=('Arial', 10, 'bold'), bd=4, command=reset)
btn2.place(x=160, y=190)
btn3 = Button(root, text=" Выход ", font=('Arial', 10, 'bold'), bd=4, command=Exit)
btn3.place(x=250, y=190)

# запускаем окно
root.mainloop()
