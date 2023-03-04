from config import openWeatherBot
import requests
from tkinter import *
import customtkinter

window = customtkinter.CTk()
window.geometry("600x600")
window.resizable(False,False)
window.title("Weather")
customtkinter.set_appearance_mode("Dark")

def add_Item():
    town = my_entry.get()
    def getWeather(town,openWeatherBot):


        codeEmoji = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"}
        try:
            req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={town}&appid={openWeatherBot}&units=metric")

            data = req.json()

            town = data["name"]
            cur_temp = data["main"]["temp"]
            descriptionWeather = data["weather"][0]["main"]
            if descriptionWeather in codeEmoji:
                dw = codeEmoji[descriptionWeather]
            else:
                dw = "Посмотри в окно"
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            my_list.insert(END,f" Погода в {town}:  {int(cur_temp)}°C : {dw}.")
            my_list.insert(END,f" Ветер {wind} м/с." )
            my_list.insert(END,f" Влажность: {humidity}%.")


        except Exception as ex:
            my_list.insert(END,"Ошибка попробуйте ввести снова")


    def main():
        getWeather(town, openWeatherBot)

    if __name__ == "__main__":
        main()


def clearAll():
    my_list.delete(0,END)

textFirst = customtkinter.CTkLabel(master=None,text="Weather by aboba555",text_color="#6C8AFF",font=("",33))
textFirst.place(x=135,y=5)

my_entry = customtkinter.CTkEntry(window,font=("Helvetica",24),width=300)
my_entry.place(x=148,y=50)

my_frame = Frame(window)
my_frame.place(x=85,y=140)

my_list = Listbox(my_frame,
                  font=("Helvetica",20),
                  width = 35,
                  height=12,
                  bd = 0,
                  activestyle="none",
                  fg = "white",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  background="#353232",
                  selectmode="EXTENDED")
my_list.pack()

add_btn = customtkinter.CTkButton(command=add_Item,text="Add",master=None)
add_btn.place(x=237,y=95)

clear_btn = customtkinter.CTkButton(command=clearAll,text="Clear",master=None,width=40)
clear_btn.place(x=400,y=95)

window.mainloop()