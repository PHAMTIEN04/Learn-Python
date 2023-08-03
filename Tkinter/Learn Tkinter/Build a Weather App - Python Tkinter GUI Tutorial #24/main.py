from tkinter import *
import requests
import json

win = Tk()
win.title("Weather App")
win.geometry("500x300")

try:
    apireq = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1A45511B-4CD6-480E-B055-A71A8ABFCAE0")
    api = json.loads(apireq.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]["Category"]["Name"]
except Exception as e:
    api = "Error.."
    
print(type(api))
print(api)
mylabel = Label(win,text= city + " Air Quality "+ str(quality) + " " + category,font=("Helvetica",20) )
mylabel.pack()
win.mainloop()