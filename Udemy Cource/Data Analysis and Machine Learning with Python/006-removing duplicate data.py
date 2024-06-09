# %%
import pandas as pd

df = pd.DataFrame({
    "flight_number": [101, 102, 102, 103, 104], 
    "airline": ["Delta", "American", "American", "Southwest", "United"], 
    "from": ["New York", "Dallas", "Dallas", "Los Angeles", "Chicago"], 
    "to": ["London", "London", "London", "London", "London"]
})

print(df)


# %%
df = df.drop_duplicates()
print(df)