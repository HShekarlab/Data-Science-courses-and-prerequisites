# %%
import pandas as pd

data = {"username": ["user_1", "user_2", "user_3", "user_4", "user_5"], 
        "age": [20, 22, 21, None, 25], 
        "gender": ["male", "female", "male", "female", "male"], 
        "level": [5, 1, 3, 2, 4]}

df = pd.DataFrame(data)
print(df)


# %%
print(df.isna())


# %%
print(df.dropna())


# %%
print(df.fillna(0))


# %%
df = pd.get_dummies(df, columns= ["gender"])
print(df)


# %%
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["age", "level"]] = scaler.fit_transform(df[["age", "level"]])
print(df)