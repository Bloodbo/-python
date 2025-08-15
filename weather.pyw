import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from datetime import datetime

API_KEY = "fecd18c530815576fd093eb555fef275"

# Функция для получения эмодзи по описанию погоды
def get_weather_emoji(description):
    description = description.lower()
    if "clear" in description:
        return "☀️ Ясно"
    elif "cloud" in description:
        return "☁️ Облачно"
    elif "rain" in description or "drizzle" in description:
        return "🌧️ Дождь"
    elif "thunderstorm" in description:
        return "⛈️ Гроза"
    elif "snow" in description:
        return "❄️ Снег"
    elif "mist" in description or "fog" in description:
        return "🌫️ Туман"
    else:
        return "🌈 Неизвестная погода"

# Функция для получения текущей погоды
def get_weather():
    city = city_entry.get()
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if weather_data.get('cod') != 200:
            raise Exception(f"Ошибка: {weather_data.get('message')}")

        city_name = weather_data['name']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        weather_emoji = get_weather_emoji(description)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        weather_info = (
            f"Город: {city_name}\n"
            f"Температура: {temp}°C (Ощущается как {feels_like}°C)\n"
            f"Влажность: {humidity}%\n"
            f"Давление: {pressure} гПа\n"
            f"Скорость ветра: {wind_speed} м/с\n"
            f"Описание: {weather_emoji}\n"
            f"Последнее обновление: {current_time}"
        )

        result_label.config(text=weather_info)

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Функция для получения прогноза погоды на 5 дней
def get_weather_forecast():
    city = city_entry.get()
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        forecast_data = response.json()

        if forecast_data.get('cod') != '200':
            raise Exception(f"Ошибка: {forecast_data.get('message')}")

        forecast_list = forecast_data['list']
        result = ""
        for forecast in forecast_list[:5]:  # Прогноз на 5 ближайших временных промежутков
            date = forecast['dt_txt']
            temp = forecast['main']['temp']
            feels_like = forecast['main']['feels_like']
            humidity = forecast['main']['humidity']
            pressure = forecast['main']['pressure']
            wind_speed = forecast['wind']['speed']
            description = forecast['weather'][0]['description']
            weather_emoji = get_weather_emoji(description)

            result += (
                f"Дата: {date}\n"
                f"Температура: {temp}°C (Ощущается как {feels_like}°C)\n"
                f"Влажность: {humidity}%\n"
                f"Давление: {pressure} гПа\n"
                f"Скорость ветра: {wind_speed} м/с\n"
                f"Описание: {weather_emoji}\n\n"
            )

        forecast_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание основного окна приложения
app = tk.Tk()
app.title("Приложение Погоды")
app.geometry("500x600")
app.configure(bg="#f0f0f0")

# Создание элементов интерфейса
title_label = tk.Label(app, text="Погодное приложение", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

tk.Label(app, text="Введите город:", font=("Arial", 14), bg="#f0f0f0", fg="#555").pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

# Рамка для отображения результата
result_frame = tk.Frame(app, bg="#e0e0e0", bd=2, relief="solid")
result_frame.pack(pady=20, fill="both", expand=True)

result_label = tk.Label(result_frame, text="", font=("Arial", 12), bg="#e0e0e0", justify="left")
result_label.pack(padx=10, pady=10)

# Кнопка для текущей погоды
tk.Button(app, text="Показать погоду", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Рамка для прогноза
forecast_frame = tk.Frame(app, bg="#e0e0e0", bd=2, relief="solid")
forecast_frame.pack(pady=10, fill="both", expand=True)

forecast_label = tk.Label(forecast_frame, text="", font=("Arial", 12), bg="#e0e0e0", justify="left")
forecast_label.pack(padx=10, pady=10)

# Кнопка для прогноза на 5 дней
tk.Button(app, text="Прогноз на 5 дней", command=get_weather_forecast, font=("Arial", 12), bg="#2196F3", fg="white", width=20).pack(pady=10)

# Запуск приложения
app.mainloop()

