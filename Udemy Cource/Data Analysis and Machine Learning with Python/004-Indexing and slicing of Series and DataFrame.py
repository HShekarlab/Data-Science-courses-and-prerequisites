# %%
import pandas as pd

data = [1000, 2000, 3000, 4000, 5000]

account_balance = pd.Series(data)
print(account_balance)


# %%
data = {"name": ["John", "Jane", "Bob", "Emily", "Mike"], 
        "account_number": [1, 2, 3, 4, 5], 
        "account_type": ["Saving", "Checking", "Saving", "Checking", "Saving"]}

customer_info = pd.DataFrame(data)
print(customer_info)

# %%
print(account_balance[0])
print(customer_info.loc[1, "name"])

# %%
print(account_balance[1:3])
print(customer_info[:2])
print(customer_info[["name", "account_number"]])

# %%
print(customer_info.iloc[1, 1])
print(customer_info.loc[1, "name"])
