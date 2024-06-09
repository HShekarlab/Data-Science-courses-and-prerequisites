# %%
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)


# %%
day_count = tips["day"].value_counts()


# %%
fig, axes = plt.subplots(1, 2, figsize= (10, 5))

# Pie Plot in the first subplot
axes[0].pie(day_count.values, 
            labels= day_count.index, 
            autopct= "%1.1f%%",
            shadow= True,
            startangle= 90)

axes[0].set_title("Pie Plot")

# Bar Plot in the second subplot
axes[1].bar(day_count.index, day_count.values,
            color= "m",
            alpha= 0.5)

axes[1].set_xlabel("Day of the week")
axes[1].set_ylabel("Count")
axes[1].set_title("Bar Plot")

plt.suptitle("Tips DataSet")
plt.show()