# %%
import pandas as pd

user_account = {"name": ["John", "Jane", "Bob", "Sara", "Mike", "Emily", "Adam"], 
                "game": ["Fortnite", "Minecraft", "Overwatch", "Fortnite", "Minecraft", "Overwatch", "League of Legends"], 
                "hours_played": [10, 6, 8, 12, 8, 4, 6]}

accounts = pd.DataFrame(user_account)
print(accounts)


# %%
grouped_df = accounts.groupby(by= "game").max()
print(grouped_df)


# %%
grouped_df = accounts.groupby(by= ["game", "name"]).sum()
print(grouped_df)


# %%
grouped_df = accounts.groupby(by= ["game", "name"]).first()
print(grouped_df)