import requests
import locale
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Set locale to Germany
locale.setlocale(locale.LC_ALL, "de_DE")

# API URL for weather data
# api_url = "https://api.openweathermap.org/data/2.5/weather"
api_url = "https://api.openweathermap.org/data/2.5/forecast"

# API key for accessing weather data
api_key = "9fa4c9c8fad5fb870c5bac828731ebbd"

# Location for which to retrieve weather data
location = "Wiesbaden"
lat = "50.078217"
lon = "8.239761"

# Resolution - X, Y
res_xy = [800, 480]

# Create a new image with given resolution and bitdepth of 1
image = Image.new("1", (res_xy[0], res_xy[1]), color=1)


def api_call():
    # call the openweathermap api using latitude, longitude, api key, set units to metric and language to german
    response = requests.get(api_url, params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric", "lang": "de"})
    print(response)

    # unpack the response
    data = response.json()
    print(data)

    # print the date and time of the first entry
    print(data["list"][0]["dt_txt"])

    datum = data["list"][0]["dt_txt"].split(" ")[0].split("-")
    print(datum)

    # get the day of the week
    dow = datetime(int(datum[0]), int(datum[1]), int(datum[2])).strftime("%a")
    print(dow)

    return data


def drawing():
    # Request weather data from API
    api_response = api_call()

    # Extract weather data
    # weather = api_response["weather"][0]["description"]
    # temperature = api_response["main"]["temp"]

    # Create element to draw on image
    draw = ImageDraw.Draw(image)

    icon = Image.open("./Icons/sunny.png")
    image.paste(icon, (400, 250))

    # Load font
    font = ImageFont.truetype("arialbd.ttf", size=30)

    # Draw weather data on image
    spacing = res_xy[0]/5
    item = 1

    while item < 6:
        draw.text((50, 50), "A", font=font, fill="black", anchor="mm")
        item += 1

    # draw.text((20, 20), "Wetter: " + weather, font=font, fill=0)
    # draw.text((20, 60), "Temperatur: " + str(temperature) + " °C", font=font, fill=0)

    # Draw time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    draw.text((650, 300), current_time, font=font, fill=0)

    # Save image
    image.save("image_with_weather.png")


drawing()
