# %%
import seaborn as sns
import plotly.express as px

df = sns.load_dataset("mpg")

print(df)


# %%
# Scatter Plot

scatter_plot = px.scatter(df, x= "horsepower", y= "mpg",
                          title= "MPG by Horsepower")

scatter_plot.update_traces(marker= dict(color= "navy", size= 7))
scatter_plot.show()


# %%
# Bar Plot

bar_plot = px.bar(df, x= "origin", y= "mpg",
                  title= "MPG by Origin")

bar_plot.update_traces(marker= dict(color= "deeppink"))
bar_plot.show()


# %%
# Histogram

hist_plot = px.histogram(df, x= "mpg",
                         nbins= 50,
                         title= "MPG Histogram")

hist_plot.update_traces(marker= dict(color= "violet"))
hist_plot.show()


# %%
# Line Plot

line_plot = px.line(df, x= "horsepower", y= "mpg",
                    title= "MPG over Horsepower")

line_plot.update_traces(marker= dict(color= "indigo"))
line_plot.show()


# %%
scatter_plot.update_layout(title= "MPG Scatter Plot by Horsepower")

scatter_plot.update_layout(xaxis_title= "Horsepower", yaxis_title= "MPG")

scatter_plot.update_traces(marker= dict(color= "lawngreen", size= 10))

scatter_plot.show()