# %%
import numpy as np
import pandas as pd
import datetime
import wbdata

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics


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


# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state= 42)


# %%
lm = LinearRegression()
lm.fit(X_train, y_train)


# %%
print(f"Coefficients : {lm.coef_}")
print(f"Intercept : {lm.intercept_}")


# %%
prediction = lm.predict(X_test)


# %%
print(f"MAE : {metrics.mean_absolute_error(y_test, prediction)}")
print(f"MSE : {metrics.mean_squared_error(y_test, prediction)}")
print(f"RMSE : {np.sqrt(metrics.mean_absolute_error(y_test, prediction))}")
print(f"R-squared value : {metrics.r2_score(y_test, prediction)}")


# %%
plt.scatter(X, y, color= "b")
plt.plot(X_test, prediction, color= "r")

plt.xlabel("Investment in Education")
plt.ylabel("GDP per Capita")
