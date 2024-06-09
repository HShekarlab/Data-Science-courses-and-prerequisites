# %%
import pandas as pd

account_holders = {"account_id": [1, 2, 3, 4], 
                   "name": ["John Smith", "Jane Doe", "Bob Johnson", "Sara Lee"], 
                   "address": ["123 Main St", "456 Park Ave", "789 Elm St", "321 0ak St"]}


accounts = pd.DataFrame(account_holders)
print(accounts)


# %%
transaction = {"account_id": [1, 2, 3, 4, 1, 2, 3], 
               "transaction_id": [101, 102, 103, 104, 105, 106, 107],
               "transaction_date": ["2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-05", "2023-05-06", "2023-05-07"], 
               "transaction_amount": [100, 50, 25, 10, 75, 25, 10]}

transaction = pd.DataFrame(transaction)
print(transaction)


# %%
merged_df = pd.merge(transaction, accounts, on= "account_id")
print(f"merged_df : {merged_df}")


# %%
accounts = accounts.set_index("account_id")
transaction = transaction.set_index("account_id")

join_df = transaction.join(accounts)
print(f"join_df : {join_df}")