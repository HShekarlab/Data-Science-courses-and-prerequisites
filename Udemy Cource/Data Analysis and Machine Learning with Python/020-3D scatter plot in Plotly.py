# %%
import seaborn as sns
import plotly.express as px

data_mpg = sns.load_dataset("mpg")


# %%
scatter_plot = px.scatter_3d(data_mpg, 
                             x= "horsepower",
                             y= "acceleration",
                             z= "mpg",
                             color= "origin",
                             title= "MPG by Horsepower, Acceleration & Origin")

scatter_plot.show()