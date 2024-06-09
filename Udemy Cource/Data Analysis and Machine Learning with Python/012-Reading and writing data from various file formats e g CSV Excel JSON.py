# %%
import os
import pandas as pd

iris_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                      names= ["sepal-length", "sepal-width", "petal-length", "petal-width", "species"])

print(iris_df)


# %%
dir_path = "./exportfilefolder"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)


# %%
iris_df.to_csv(os.path.join(dir_path, "iris_data.csv"), index= False)
iris_df.to_excel(os.path.join(dir_path, "iris_data.xlsx"), index= False)
iris_df.to_json(os.path.join(dir_path, "iris_data.json"))


# %%
files = os.listdir(dir_path)
print(files)


# %%
iris_from_json = pd.read_json(os.path.join(dir_path, "iris_data.json"))
print(iris_from_json)


# %%
iris_from_excel = pd.read_excel(os.path.join(dir_path, "iris_data.xlsx"))
print(iris_from_json)