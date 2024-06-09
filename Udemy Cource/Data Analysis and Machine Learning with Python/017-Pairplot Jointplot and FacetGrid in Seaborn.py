# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data.data, columns= data.feature_names)
df["target"] = data.target

sns.pairplot(df, hue= "target")
plt.show()


# %%
sns.jointplot(data= df, x= "sepal length (cm)", y= "sepal width (cm)",
              kind= "scatter")

plt.show()


# %%
g = sns.FacetGrid(df, col= "target")
g.map(sns.scatterplot, "sepal length (cm)", "sepal width (cm)")

plt.show()
# %%
