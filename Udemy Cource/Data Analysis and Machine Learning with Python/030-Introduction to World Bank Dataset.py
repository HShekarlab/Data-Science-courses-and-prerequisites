# %%
import numpy as np
import pandas as pd
import datetime
import wbdata

from sklearn.model_selection import train_test_split


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