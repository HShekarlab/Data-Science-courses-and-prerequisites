# %%
import numpy as np
import pandas as pd

data = {"date": ["2021-02-01", "2024-02-02", "2024-02-03"]}

df = pd.DataFrame(data)
print(df)


# %%
df["date"] = pd.to_datetime(df["date"])
print(df)


# %%
from pytz import timezone

eastern_time = pd.Timestamp("2024-03-01 00:00:00", tz= "Us/Eastern")

utc_time = eastern_time.tz_convert("UTC")
print(utc_time)

# %%
date_rng = pd.date_range(start= "1/1/2024", end= "10/1/2024", freq= "H")

df = pd.DataFrame(date_rng, columns= ["date"])
print(df)


# %%
df["date"] = np.random.randint(0, 100, size= (len(date_rng)))

df_daily = df.resample("D", on= "date").mean()
print(df_daily)


# %%
date = pd.to_datetime("2024-06-03")

print(date.year)
print(date.month)
print(date.day)