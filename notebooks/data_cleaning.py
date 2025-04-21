import pandas as pd
import numpy as np

today = pd.to_datetime("2025-04-19")

data_frame=pd.read_csv(r"data\Netflix_Userbase.csv")

data_frame['Join Date'] = pd.to_datetime(data_frame['Join Date'], format='%d-%m-%y')

np.random.seed(42)
data_frame['Last Payment Date'] = data_frame['Join Date'] + pd.to_timedelta(
    np.random.randint(30, 700, size=len(data_frame)), unit='D'
)
data_frame['Last Payment Date'] = data_frame['Last Payment Date'].apply(lambda x: min(x, today))

data_frame['plan_duration_days'] = data_frame['Plan Duration'].str.extract(r'(\d+)').astype(int) * 30

data_frame['days_since_last_payment'] = (today - data_frame['Last Payment Date']).dt.days
data_frame['user_lifetime_days'] = (today - data_frame['Join Date']).dt.days

data_frame['is_churned'] = (data_frame['days_since_last_payment'] > data_frame['plan_duration_days']).astype(int)

data_frame.to_csv(r"data\Netflix_Userbase.csv", index=False)