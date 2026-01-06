# ⚡ Energy Consumption Forecasting

A machine learning project that predicts **future hourly energy consumption**
using historical data, weather information, and time-based features.

This project is built with a **time-series forecasting mindset**, similar to
weather forecasting systems.

---

## 📌 Problem Statement

Accurately forecasting energy consumption is crucial for:
- Power grid management
- Cost optimization
- Demand planning

The goal of this project is to predict **future energy usage** using:
- Historical energy data
- Weather features (temperature, humidity)
- Time-based patterns (hour, day, seasonality)

---

## 🧠 Approach

1. **Exploratory Data Analysis**
   - Hourly energy consumption data
   - Weather impact analysis

2. **Feature Engineering**
   - Time features (hour, day of week, month, weekend)
   - Lag features (1 hour, 24 hours, 168 hours)
   - Rolling statistics (24h, 7-day averages)

3. **Modeling**
   - Baseline (naive forecast)
   - Linear Regression
   - Random Forest Regressor (final model)

4. **Evaluation**
   - Time-based train/test split
   - Mean Absolute Error (MAE)

5. **Forecasting**
   - Recursive multi-step forecasting
   - Next 24-hour energy prediction

---

## 📊 Results

| Model | MAE |
|-----|-----|
Baseline | ~15.37 |
Linear Regression | ~10.90 |
Random Forest | **~3.13** |

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## 📁 Project Structure
## 📁 Project Structure

```
energy-consumption-forecast/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   ├── features.py
│   └── predict.py
│
├── models/
│   └── energy_forecast_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Future Improvements

- Integrate real weather forecasts
- Add XGBoost / LightGBM
- Build REST API for predictions
- Deploy using Docker

---

## 👤 Author

**Avanit Dobariya**  
Aspiring Data Scientist / ML Engineer