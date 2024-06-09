# %%
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")


# %%
sns.scatterplot(data= data, x= "total_bill", y= "tip")

sns.set_style("darkgrid")
sns.set_context("poster")

plt.xlabel("Totall Bill", fontsize= 18)
plt.ylabel("Tip", fontsize= 18)
plt.title("Total bill vs Tip", fontsize= 24)

plt.show()