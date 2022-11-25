from tkinter import *
import requests


def get_coordinates():
    params = {
        "city_name": location.get(),
        "API key": "182a622e91346b878a9e987e156944c6"
    }
    city_name = params["city_name"]
    api_key = params["API key"]

    response = requests.get(
        url=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}")
    response.raise_for_status()
    data = response.json()
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]
    coordinates = (latitude, longitude)
    print(coordinates)


window = Tk()
window.title("Spot the Station")
window.config(width=600, height=600, padx=40, pady=40)

location_text = Label(text="Your location: ")
location_text.grid(row=0, column=0)
location = Entry()
location.grid(row=0, column=1)
generate_button = Button(text="Find out the opportunity", padx=20, pady=20, command=get_coordinates)
generate_button.grid(row=1, column=0, columnspan=2)
iss_info = Label(text="The nearest sighting opportunity is", font=("Arial",14, "bold"))
iss_info.grid(row=2, column=0, columnspan=2)



window.mainloop()
