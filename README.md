Powering Villages, Empowering Lives – Smart Energy Planning Using AI & Satellite Data
#This predicts renewable energy potential for villages in India using:
#Satellite Data
#AI Solar Prediction
#Weather Forecasts
It plans energy usage, storage, and distribution, helping reduce fossil fuel dependence and promoting sustainable electricity.
“Every house gets solar power, every village gets a wind turbine, and energy is used smartly according to production and storage.”

| Feature                    | Description                               
| -------------------------- | ------------------------------------------ 
| Satellite & Weather Data   | NASA POWER API + Open-Meteo API            
| AI Solar Prediction        | 7-day solar energy forecast                
| Wind Energy Prediction     | Wind turbine output calculation           
| Energy Planning & Storage  | Battery management & demand vs. supply     
| Smart Recommendations      | EV charging, solar cookers, stove planning 
| Government-Style Dashboard | Interactive map & charts                   

 Example Workflow

1. Enter village coordinates→ fetch satellite & weather data
2. Calculate solar & wind energy
3. AI predicts 7-day energy output
4. Compute village electricity demand & storage requirements
5. Generate energy usage plan for houses, EVs, and cooking

 Energy Calculations

**Solar Energy:**

```python
Energy (kWh/day) = Solar Radiation × Panel Area × Efficiency
```

**Wind Energy:**

```python
Power (kW) = 0.5 × Air Density × Rotor Area × Wind³
```

**Energy Planning:**

* Daily demand = Number of houses × 6 kWh
* Surplus → Battery storage
* Low production → Use stored energy

---

## 🎨 Dashboard Highlights

* **Map:** Interactive district solar potential (🟢 High, 🟡 Medium, 🔴 Low)
* **Panel:** Shows predicted solar energy, wind speed, and renewable score
* **Chart:** 7-day solar energy forecast using Chart.js
* **Globe:** 3D India renewable energy visualization with Three.js

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **AI/ML:** scikit-learn Linear Regression
* **APIs:** NASA POWER, Open-Meteo, OpenStreetMap
* **Frontend:** HTML, CSS, JS, Leaflet, Chart.js, Three.js
* **Database:** SQLite
 Why This Project Matters
* Promotes **renewable energy adoption** at village & household level
* Reduces **pollution & fossil fuel usage**
* Supports **EV charging & clean cooking**
* Enables **smart energy storage and planning**
 Getting Started
# Clone the repository
git clone <your-repo-link>
# Install dependencies
pip install django pandas scikit-learn requests
# Run the server
python manage.py runserver
Open browser: `http://127.0.0.1:8000`
Enter latitude & longitude** → see renewable energy plan!
Inspiration
.This project is inspired by ISRO, NASA, and NREL research in renewable energy planning and smart grids.
.Smart renewable energy for villages is the key to a sustainable and pollution-free future.


---

Harini, if you want, I can also **design a ready-to-paste GitHub README with images, icons, colored sections, and a live demo GIF** so it looks like a **professional government research dashboard** — this will **definitely impress internship evaluators**.

Do you want me to make that full visual GitHub-ready version next?
