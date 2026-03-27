import requests

def get_satellite_data(lat, lon):

    try:

        solar_url = f"https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=ALLSKY_SFC_SW_DWN&latitude={lat}&longitude={lon}&format=JSON"

        solar_data = requests.get(solar_url).json()

        solar = solar_data.get("properties", {}) \
                          .get("parameter", {}) \
                          .get("ALLSKY_SFC_SW_DWN", {}) \
                          .get("ANN", 5)

    except:
        solar = 5


    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=wind_speed_10m,cloud_cover,temperature_2m"

    weather = requests.get(weather_url).json()

    wind = weather.get("current", {}).get("wind_speed_10m", 3)
    cloud = weather.get("current", {}).get("cloud_cover", 20)
    temp = weather.get("current", {}).get("temperature_2m", 30)

    return solar, wind, cloud, temp