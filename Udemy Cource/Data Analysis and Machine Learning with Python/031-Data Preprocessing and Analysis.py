# %%
import numpy as np
import pandas as pd
import datetime
import wbdata

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression


# %%
data_dates = (datetime.datetime(2023, 1, 2), datetime.datetime(2024, 1, 2))
gdp_data = wbdata.get_data("NY.GDP.PCAP.CD", date_date= data_dates)
edu_data = wbdata.get_data("SE.XPD.TOTL.GD.ZS", data_date = data_dates)
df_gdp = pd.DataFrame(gdp_data)
df_edu = pd.DataFrame(edu_data)


# %%
df_gdp["country"] = [x.get("value") for x in list(df_gdp["country"])]
df_edu["country"] = [x.get("value") for x in list(df_edu["country"])]

df_gdp["value"] = [x for x in list(df_gdp["value"])]
df_edu["value"] = [x for x in list(df_edu["value"])]


# %%
merge_df = pd.merge(df_gdp, df_edu, on= ["country"])

print(merge_df.columns)
merge_df.rename(columns= {"value_x": "gdp",
                          "value_y": "education"},
                          inplace= True)


# %%
print(merge_df.isna().sum())


# %%
merge_df = merge_df.dropna(axis= 0, how= "any")


# %%
scaler = MinMaxScaler()

merge_df[["education", "gdp"]] = scaler.fit_transform(merge_df[["education", "gdp"]])

X = merge_df["education"]
y = merge_df["gdp"]

