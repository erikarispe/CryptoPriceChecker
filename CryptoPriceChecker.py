#This will launch a tkinter window that will display the current time and prices of the symbols used as an example, it will automatically refresh every 30 seconds with the updated time and prices, after the initial launch.
#It will also print a message in the terminal once it has refreshed. 


import requests
import json
from datetime import datetime, timezone
from tzlocal import get_localzone
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# code for app
app = tk.Tk()

backgroundimageload = Image.open('/Users/erikarispe/Desktop/Resumehtml/Crytpo price checker/CryptoPriceChecker/images/bgimage.png')
resizedbackgroundimageload = backgroundimageload.resize((800, 500))
backgroundimage = ImageTk.PhotoImage(resizedbackgroundimageload)

backgroundimage_label = tk.Label(app, image=backgroundimage)
backgroundimage_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variables to store data
symbol1 = ''
price1 = ''
symbol2 = ''
price2 = ''
symbol3 = ''
price3 = ''

# Function to refresh the prices.
def refresh_prices():
    global symbol1, price1, symbol2, price2, symbol3, price3

    # First crypto symbol
    symbol1 = 'LTCBTC'
    api_url1 = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol1)
    response1 = requests.get(api_url1, headers={'X-Api-Key': 'fPP62n6nIWz78cl+KUbhRQ==rfRrQKgwOpJ0jSUb'})

    updated_response1 = response1.text

    # Parse the JSON string
    data1 = json.loads(updated_response1)

    # Access specific values
    timestamp1 = data1['timestamp']
    price1 = data1['price']

    # Convert timestamp to datetime object in UTC
    dt_object1_utc = datetime.fromtimestamp(timestamp1, tz=timezone.utc)

    # Get the user's local timezone
    desired_timezone1 = get_localzone()
    local_time1 = dt_object1_utc.astimezone(desired_timezone1)

    # Format the time in 12-hour format with AM/PM
    formatted_time1 = local_time1.strftime('%I:%M %p')

    # Second crypto symbol
    symbol2 = 'BTCUSD'
    api_url2 = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol2)
    response2 = requests.get(api_url2, headers={'X-Api-Key': 'fPP62n6nIWz78cl+KUbhRQ==rfRrQKgwOpJ0jSUb'})

    updated_response2 = response2.text

    # Parse the JSON string
    data2 = json.loads(updated_response2)

    # Access specific values
    timestamp2 = data2['timestamp']
    price2 = data2['price']

    # Convert timestamp to datetime object in UTC
    dt_object2_utc = datetime.fromtimestamp(timestamp2, tz=timezone.utc)

    # Get the user's local timezone
    desired_timezone2 = get_localzone()
    local_time2 = dt_object2_utc.astimezone(desired_timezone2)

    # Format the time in 12-hour format with AM/PM
    formatted_time2 = local_time2.strftime('%I:%M %p')

    # Third crypto symbol
    symbol3 = 'ETHUSD'
    api_url3 = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol3)
    response3 = requests.get(api_url3, headers={'X-Api-Key': 'fPP62n6nIWz78cl+KUbhRQ==rfRrQKgwOpJ0jSUb'})

    updated_response3 = response3.text

    # Parse the JSON string
    data3 = json.loads(updated_response3)

    # Access specific values
    timestamp3 = data3['timestamp']
    price3 = data3['price']

    # Convert timestamp to datetime object in UTC
    dt_object3_utc = datetime.fromtimestamp(timestamp3, tz=timezone.utc)

    # Get the user's local timezone
    desired_timezone3 = get_localzone()
    local_time3 = dt_object3_utc.astimezone(desired_timezone3)

    # Format the time in 12-hour format with AM/PM
    formatted_time3 = local_time3.strftime('%I:%M %p')

    # Update labels with new data
    home_page_time.config(text=f"Time: {formatted_time3}")
    symbol_1.config(text=f"{symbol1}, Price: {price1}")
    symbol_2.config(text=f"{symbol2}, Price: {price2}")
    symbol_3.config(text=f"{symbol3}, Price: {price3}")

    # Print a message in the terminal
    print("Prices refreshed at", datetime.now())

    # Schedule the next refresh after 30 seconds
    app.after(30000, refresh_prices)

# Labels for displaying data
home_page_time = tk.Label(app, text="Time:", font=("Helvetica", 14), fg="white", bg="blue")
home_page_time.pack(pady=30)

symbol_1 = tk.Label(app, text="", font=("Helvetica", 14), fg="white", bg="blue")
symbol_1.pack(pady=10)

symbol_2 = tk.Label(app, text="", font=("Helvetica", 14), fg="white", bg="blue")
symbol_2.pack(pady=10)

symbol_3 = tk.Label(app, text="", font=("Helvetica", 14), fg="white", bg="blue")
symbol_3.pack(pady=10)

# Initial call to start the refresh process
refresh_prices()

# code for app
app.geometry('800x500')
app.title('Crypto Prices')
app.resizable(False, False)

# this will be able to run the application
app.mainloop()
