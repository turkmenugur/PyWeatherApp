from tkinter import messagebox
from tkinter import *
import requests
import apiKeyFile

window = Tk()
window.title("Weather")
window.geometry("500x300")

url = "http://api.weatherapi.com/v1/current.json"
api_key = apiKeyFile.api_key

# Global etiketler
image_label = None
city_label = None
temperature_label = None
description_label = None

def get_data():
    global city_label, temperature_label, description_label, image_label
    city = location.get()

    parameters = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        # API'ye GET isteğinin gönderilmesi
        response = requests.get(url=url, params=parameters)

        # Yanıtı kontrol edip ve hava durumu verilerini alma
        if response.status_code == 200:
            weather_data = response.json()

            # Hava durumu verilerinin işlenmesi
            temperature = weather_data["current"]["temp_c"]
            condition = weather_data["current"]["condition"]["text"]

            # Etiketlerin güncellenmesi
            city_label.config(text=f"{city}")
            temperature_label.config(text=f"{temperature}°C")
            description_label.config(text=f"{condition}")

            # Resmin güncellenmesi
            if condition == "Sunny":
                image = PhotoImage(file="assets/sunny.png")
            elif condition == "Cloudy":
                image = PhotoImage(file="assets/cloudy.png")
            elif condition == "Rainy":
                image = PhotoImage(file="assets/rainy.png")
            elif condition == "Partly cloudy":
                image = PhotoImage(file="assets/partly-cloudy.png")
            elif condition == "Foggy":
                image = PhotoImage(file="assets/foggy.png")
            elif condition == "Snowy":
                image = PhotoImage(file="assets/snowy.png")
            elif condition == "Storming":
                image = PhotoImage(file="assets/storming.png")
            elif condition == "Windy":
                image = PhotoImage(file="assets/windy.png")
            elif condition == "Overcast":
                image = PhotoImage(file="assets/overcast.png")
            elif condition == "Mist":
                image = PhotoImage(file="assets/mist.pngpwd"
                                        "")
            else:
                image = PhotoImage(file="assets/sunny.png")

            image_label.config(image=image)
            image_label.image = image
            image_label.pack(side="left")

            # Etiketlerin yeniden gösterilmesi
            for label in [city_label, temperature_label, description_label]:
                label.pack(side="top")
        else:
            print("Hava durumu verisi alınamadı. API yanıtı:", response.status_code)
            messagebox.showerror(title="Hata!", message=f"Hava durumu verisi alınamadı. API yanıtı: {response.status_code}")
    except:
        messagebox.showerror(title="Hata!", message=f"Hava durumu bilgisi alma başarısız oldu")

#ui
frame = Frame(window)
frame.pack(side="top", padx=(10,0), pady=(10,10),fill='x')

label_for_frame = Label(frame,text="Konum:")
label_for_frame.pack(side="left",padx=(10,0), pady=(10,10))

location = Entry(frame)
location.pack(side="left",padx=(10,0), pady=(10,10))

get_data_button = Button(frame, text="Ara",width=10,command=get_data)
get_data_button.pack(side="left",padx=(10,0), pady=(10,10))

def show_weather_frame(weather_info_frame):
    city_label = Label(weather_info_frame, text="City")
    city_label.pack(side="top")
    temperature_label = Label(weather_info_frame, text="Temperature")
    temperature_label.pack(side="top")
    description_label = Label(weather_info_frame, text="Description")
    description_label.pack(side="top")

weather_frame = Frame(window)
weather_frame.pack(side="top", padx=(10,0), pady=(10,10),fill='x')

#image = PhotoImage(file="foggy.png")

weather_info_frame = Frame(weather_frame)
weather_info_frame.pack(side="left", padx=(10,0), pady=(10,10),fill='x')

image_label = Label(weather_frame)
image_label.pack(side="left")

weather_info_frame = Frame(weather_frame)
weather_info_frame.pack(side="left")

show_weather_frame(weather_info_frame=weather_info_frame)
for label in weather_info_frame.winfo_children():
    label.pack_forget()

# Global etiketlerin tanımlanması
city_label = Label(weather_info_frame, text="City")
temperature_label = Label(weather_info_frame, text="Temperature")
description_label = Label(weather_info_frame, text="Description")

window.mainloop()
