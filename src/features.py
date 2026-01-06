import pandas as pd

def create_features(df):
    df = df.copy()

    # time-based features
    df['hour'] = df.index.hour
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

    # lag features
    df['energy_lag_1'] = df['energy_consumption'].shift(1)
    df['energy_lag_24'] = df['energy_consumption'].shift(24)
    df['energy_lag_168'] = df['energy_consumption'].shift(168)

    # rolling features
    df['energy_roll_24'] = df['energy_consumption'].rolling(24).mean()
    df['energy_roll_168'] = df['energy_consumption'].rolling(168).mean()

    return df
