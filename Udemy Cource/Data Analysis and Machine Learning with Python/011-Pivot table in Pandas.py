# %%
import pandas as pd

df = pd.DataFrame({
    "Airline": ["Delta", "Air Canada", "United", "American"], 
    "Destination": ["New York", "Toronto", "Vancouver", "Montreal"],
    "Bookings": [12, 34, 56, 78]
})

print(df)


# %%
pivot_table = df.pivot_table(index= "Airline", 
                             columns= "Destination", 
                             values= "Bookings")

print(pivot_table)