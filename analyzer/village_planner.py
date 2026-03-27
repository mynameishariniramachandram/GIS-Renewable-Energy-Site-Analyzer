def plan_village(houses,solar,wind):

    house_demand=6

    village_demand=houses*house_demand

    panel_output=solar*10*0.18

    panels=village_demand/panel_output

    wind_energy=0.5*1.225*10*(wind**3)

    return{

    "demand":village_demand,
    "panels":round(panels),
    "wind_energy":round(wind_energy,2),
    "turbines":1

    }