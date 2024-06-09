# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
#                     names= ["sepal-length", "sepal-width", "petal-length", "petal-width", "species"])

# print(data)

data = load_iris()

col_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "species"]

data = pd.DataFrame(data.data, columns= data.feature_names)

print(data)



# %%
# Line Plot

plt.plot(data["sepal-length"], label= "sepal-length")
plt.plot(data["sepal-width"], label= "sepal-width")

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Plot")

plt.legend()
plt.show()


# %%
# Scatter Plot

plt.scatter(data["sepal-length"], data["sepal-width"], label= "sepal")
plt.scatter(data["petal-length"], data["petal-width"], label= "petal")

plt.xlabel("Length")
plt.ylabel("Width")
plt.title("Scatter Plot")

plt.legend()
plt.show()


# %%
# Pie Plot

sizes = data["Species"].value_counts()

plt.pie(sizes, labels= sizes.index, autopct= "%0.1f%%")
plt.title("Pie Plot")
plt.show()


# %%
# Histogram

plt.hist(data["sepal-length"], bins= 10, alpha= 0.5, label= "Sepal Length")
plt.hist(data["sepal-width"], bins= 10, alpha= 0.5, label= "Sepal Width")

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Plot")

plt.legend()
plt.show()

