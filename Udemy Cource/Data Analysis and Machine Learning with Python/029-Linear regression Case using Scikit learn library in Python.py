# %%
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# %%
data = sns.load_dataset("tips")
print(data)


# %%
X = data[["total_bill"]]
y = data["tip"]


# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state= 33)


# %%
model = LinearRegression()

model.fit(X_train, y_train)


# %%
y_predict = model.predict(X_test)


# %%
plt.scatter(X_test, y_test, color= "b")
plt.plot(X_test, y_predict, color= "lime", linewidth= 2)

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Linear Regression of Tips vs Total Bill")


# %%
print(f"Model Intercept : {model.intercept_}")
print(f"Model Coefficients : {model.coef_}")
print(f"Model Score : {model.score(X_test, y_test)}")