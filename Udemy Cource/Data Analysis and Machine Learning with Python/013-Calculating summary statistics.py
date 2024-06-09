# %%
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data.data, columns= data.feature_names)
df["target"] = data.target

print(df)


# %%
print(df.describe())


# %%
print("********** mean **********")
print(df.mean())


# %%
print("********** median **********")
print(df.median())


# %%
print("********** mode **********")
print(df.mode())


# %%
print("********** max **********")
print(df.max())


# %%
print("********** min **********")
print(df.min())


# %%
print("********** std **********")
print(df.std())


# %%
print("********** var **********")
print(df.var())