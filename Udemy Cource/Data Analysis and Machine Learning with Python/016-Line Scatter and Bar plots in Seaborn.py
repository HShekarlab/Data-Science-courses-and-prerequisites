# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

mpg = sns.load_dataset("mpg")

sns.lineplot(data= mpg,
             x= "acceleration",
             y= "horsepower")

plt.xlabel("acceleration")
plt.ylabel("horsepower")
plt.title("Mpg Dataset")

plt.show()


# %%
taxis = sns.load_dataset("taxis")

sns.scatterplot(data= taxis,
                x= "distance",
                y= "tip")

plt.xlabel("Distance")
plt.ylabel("Tip")
plt.title("Taxis Dataset")

plt.show()


# %%
data = load_iris()

df = pd.DataFrame(data.data, columns= data.feature_names)
df["target"] = data.target

sns.barplot(data= df, x= "target", y= "sepal length (cm)", palette= "rocket")

plt.xlabel("Target")
plt.ylabel("Sepal Length")
plt.title("Sepal Length by Target")

plt.show()