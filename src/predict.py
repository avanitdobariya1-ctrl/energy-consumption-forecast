import joblib
import pandas as pd
from pathlib import Path

FEATURES = [
    'temperature',
    'humidity',
    'hour',
    'day_of_week',
    'month',
    'is_weekend',
    'energy_lag_1',
    'energy_lag_24',
    'energy_lag_168',
    'energy_roll_24',
    'energy_roll_168'
]


def load_model():
    project_root = Path(__file__).resolve().parent.parent
    model_path = project_root / "models" / "energy_forecast_model.pkl"
    return joblib.load(model_path)


def forecast_next_hours(model, history, future_weather, hours=24):
    history = history.copy()
    predictions = []

    for i in range(hours):
        next_time = history.index[-1] + pd.Timedelta(hours=1)

        row = {
            'temperature': future_weather.iloc[i]['temperature'],
            'humidity': future_weather.iloc[i]['humidity'],
            'hour': next_time.hour,
            'day_of_week': next_time.dayofweek,
            'month': next_time.month,
            'is_weekend': int(next_time.dayofweek in [5, 6]),
            'energy_lag_1': history.iloc[-1]['energy_consumption'],
            'energy_lag_24': history.iloc[-24]['energy_consumption'],
            'energy_lag_168': history.iloc[-168]['energy_consumption'],
            'energy_roll_24': history['energy_consumption'].iloc[-24:].mean(),
            'energy_roll_168': history['energy_consumption'].iloc[-168:].mean()
        }

        X_next = pd.DataFrame([row])[FEATURES]
        y_next = model.predict(X_next)[0]

        predictions.append((next_time, y_next))

        history.loc[next_time] = history.iloc[-1]
        history.loc[next_time, 'energy_consumption'] = y_next

    return (
        pd.DataFrame(predictions, columns=['datetime', 'predicted_energy'])
        .set_index('datetime')
    )