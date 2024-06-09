# %%
import pandas as pd

data = {"book_id": [1, 2, 3, 4, 5, 6], 
        "destination": ["New York", "Los Angeles", "Chicago", "New York", "Chicago", "Los Angeles"], 
        "price": [500, 450, 300, 550, 325, 475]}

df = pd.DataFrame(data)
print(df)


# %%
print(df[df["destination"] == "New York"])


# %%
print(df.sort_values(by= "price", ascending= False))


# %%
df = df.sort_index(axis= 0)
print(df)


# %%
print(df.groupby("destination")["price"].mean())