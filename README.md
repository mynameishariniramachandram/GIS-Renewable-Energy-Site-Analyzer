
# 🌞 Powering Villages, Empowering Lives

**Smart Energy Planning Using AI & Satellite Data**

Predict renewable energy potential for villages in India using:
`#SatelliteData #AISolarPrediction #WeatherForecasts`

> “Every house gets solar power, every village gets a wind turbine, and energy is used smartly according to production and storage.”

---

## ⚡ Features

| Feature                            | Description                                |
| ---------------------------------- | ------------------------------------------ |
| ☁️ **Satellite & Weather Data**    | NASA POWER API + Open-Meteo API            |
| 🤖 **AI Solar Prediction**         | 7-day solar energy forecast using ML       |
| 🌬️ **Wind Energy Prediction**     | Wind turbine output calculation            |
| 🔋 **Energy Planning & Storage**   | Battery management & demand vs. supply     |
| 🔌 **Smart Recommendations**       | EV charging, solar cookers, stove planning |
| 🏛️ **Government-Style Dashboard** | Interactive map & charts for policymakers  |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![APIs](https://img.shields.io/badge/APIs-NASA%20POWER%20%7C%20Open-Meteo-blue?style=for-the-badge)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge)

---

## 🔄 Workflow

```mermaid
flowchart TD
    A[Enter village coordinates] --> B[Fetch satellite & weather data]
    B --> C[Calculate solar & wind energy]
    C --> D[AI predicts 7-day energy output]
    D --> E[Compute village electricity demand & storage]
    E --> F[Generate energy usage plan for houses, EVs, cooking]
    F --> G[View interactive dashboard]
```

---

## 🔬 Energy Calculations

**Solar Energy:**

```text
Energy (kWh/day) = Solar Radiation × Panel Area × Efficiency
```

**Wind Energy:**

```text
Power (kW) = 0.5 × Air Density × Rotor Area × Wind³
```

**Energy Planning:**

* Daily demand = Number of houses × 6 kWh
* Surplus → Battery storage
* Low production → Use stored energy

---

## 🎨 Dashboard Highlights

* **Map:** Interactive district solar potential (🟢 High, 🟡 Medium, 🔴 Low)
* **Panel:** Predicted solar energy, wind speed, renewable score
* **Chart:** 7-day solar energy forecast using Chart.js
* **Globe:** 3D India renewable energy visualization with Three.js

---

## 🖼️ Output Screenshots

**Main Dashboard:**
![Main Dashboard](images/main/main.png)

**Energy Results:**
![Result Dashboard](images/result/result.png)

---

## 🚀 Getting Started

```bash
# Clone repository
git clone <repo-url>

# Install dependencies
pip install django pandas scikit-learn requests

# Run server
python manage.py runserver
```

Open browser: [http://127.0.0.1:8000](http://127.0.0.1:8000) → Enter latitude & longitude → see renewable energy plan!

---

## 🌱 Impact

* Promotes renewable energy adoption at village & household level
* Reduces pollution & fossil fuel usage
* Supports EV charging & clean cooking
* Enables smart energy storage and planning

---

## 💡 Inspiration

Inspired by **ISRO**, **NASA**, and **NREL** research in renewable energy planning and smart grids.
Smart renewable energy for villages is key to a **sustainable, pollution-free future**.

---

## 🎯 Next Steps / Ideas

* Add **real-time weather updates** for dynamic planning
* Include **battery optimization** for peak hours
* Expand dashboard to show **district-wise comparison**
* Generate **PDF reports** for village energy plans

---
