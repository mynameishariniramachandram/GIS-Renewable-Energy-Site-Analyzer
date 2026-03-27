import requests

def energy_forecast(lat,lon):

    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,wind_speed_10m_max"

    data=requests.get(url).json()

    forecast=[]

    for i in range(len(data["daily"]["time"])):

        temp=data["daily"]["temperature_2m_max"][i]

        wind=data["daily"]["wind_speed_10m_max"][i]

        solar=5+(temp*0.02)

        energy=solar*10*0.18

        forecast.append({

        "date":data["daily"]["time"][i],
        "energy":round(energy,2)

        })

    return forecast