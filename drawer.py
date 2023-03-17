import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# API URL for weather data
api_url = "https://api.openweathermap.org/data/2.5/weather"

# API key for accessing weather data
api_key = "9fa4c9c8fad5fb870c5bac828731ebbd"

# Location for which to retrieve weather data
location = "Wiesbaden"
lat = "50.078217"
lon = "8.239761"


def drawing():
    # Request weather data from API
    response = requests.get(api_url, params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric"})
    print(response)
    data = response.json()
    print(data)

    # Extract weather data
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    # Load image
    image = Image.new("1", (800, 480), color=1)

    # draw 3px wide lines to separate quadrants
    draw = ImageDraw.Draw(image)
    draw.line((0, 240, 800, 240), fill=0, width=3)  # horizontal line
    draw.line((400, 0, 400, 480), fill=0, width=3)  # vertical line

    # Load font
    font = ImageFont.truetype("VT323-Regular.ttf", size=30)

    # Draw weather data on image
    draw = ImageDraw.Draw(image)
    draw.text((20, 20), "Weather: " + weather, font=font, fill=0)
    draw.text((20, 40), "Temperature: " + str(temperature) + " °C", font=font, fill=0)

    # Draw time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    draw.text((650, 300), current_time, font=font, fill=0)

    # Save image
    image.save("image_with_weather.bmp")
