# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/Concrete_Data.xls")

print(data)


# %%
print(data.columns)


# %%
print(data.info())


# %%
print(data.describe())


# %%
print(data.describe)


# %%
print(data.head(3))


# %%
print(data.dtypes)


# %%
print(data.isna().sum())


# %%
print(data.duplicated().sum())


# %%
sns.heatmap(data.corr(), annot= True)
plt.show()


# %%
sns.pairplot(data)


# %%
sns.scatterplot(data= data,
                x= "Water  (component 4)(kg in a m^3 mixture)",
                y= "Superplasticizer (component 5)(kg in a m^3 mixture)")


# %%
sns.jointplot(data= data,
              x= "Water  (component 4)(kg in a m^3 mixture)",
              y= "Superplasticizer (component 5)(kg in a m^3 mixture)",
              color= "b")  

# plt.show()              