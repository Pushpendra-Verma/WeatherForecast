import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6d258615fc1cad10429b5db2d4888fd0"

    json_data = requests.get(api).json()  # doubt line
    # print(str(json_data['coord']['lon']))
    # print(str(json_data['coord']['lat']))

    lon = str(json_data['coord']['lon'])
    lat = str(json_data['coord']['lat'])

    api_daily = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&exclude=hourly,alerts,minutely,current&appid=6d258615fc1cad10429b5db2d4888fd0"
    json_data_daily = requests.get(api_daily).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    # min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    clouds = json_data['clouds']['all']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    rain_daily = json_data_daily['daily'][0]['weather'][0]['description']
    temp_daily = int(json_data_daily['daily'][0]['temp']['max'] - 273.15)
    rain_mm = json_data_daily['daily'][0]['rain']


    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: "+ sunrise + "\n" + "Sunset: " + sunset + "\n" + "clouds:" + str(clouds) + "%"+ "\n" + "-----------------------------" + "\n" + "Tomorrow: " + "\n" + "rain: " + str(rain_daily) + " " + str(rain_mm) + "mm" + "\n " + "Max. Temperature: " + str(temp_daily)+ "degree"

    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("500x700")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)  # Inherited the canvas class
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()