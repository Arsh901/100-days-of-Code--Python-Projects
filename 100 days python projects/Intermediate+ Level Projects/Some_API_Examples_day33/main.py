from tkinter import *
import requests
from datetime import *

"""File is divided into 3 different codes. While trying one code keep the rest as comments. 
                    Though 2nd and 3rd can be can together"""


"""<-------------------------------Kanye West Quotes-------------------------------->"""
# def get_quote():
#     quote = requests.get(url="https://api.kanye.rest")
#     quote.raise_for_status()
#     data = quote.json()
#     canvas.itemconfig(quote_text, text=data["quote"])
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
#
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

"""<------------------------------Space Station location finder--------------------------------->"""
# my_lat, my_long = 28.472027, 77.089539
# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#
#     data = response.json()
#
#     longitude =  float(data["iss_position"]["longitude"])
#     latitude =  float(data["iss_position"]["latitude"])
#
#     print(f"Longitude = {longitude}")
#     print(f"Latitude = {latitude}")
#     if my_long-5<= longitude <=my_long+5 and my_lat-5<=latitude<=my_lat+5:
#         return True
#
#
"""<--------------------------Sunset and Sunrise------------------------->"""
# def is_night():
#     inp = {
#         "lat" : 28.472027,
#         "lng" : 77.089539,
#         "formatted" : 0
#     }
#     response = requests.get(url="https://api.sunrise-sunset.org/json",params=inp)
#     response.raise_for_status()
#     data = response.json()
#     print(data)
#     sunrise = int(data["results"]["sunrise"].split("T")[0].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[0].split(":")[0])
#
#     time_now = datetime.now().hour
#     if sunset<= time_now or time_now<=sunrise:
#         return True







