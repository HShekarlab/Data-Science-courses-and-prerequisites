# %%
import numpy as np

# Create a Numpy array

stock_price = np.array([10.0, 12.0, 15.0, 11.0, 8.0, 9.0, 7.0, 5.0, 6.0, 6.0, 4.0, 2.0, 1.0, 3.0])
print(stock_price)


# %%
# A. Creating arrays
# Create a 2-dimentional Array of shape (7, 2)

price_2d = stock_price.reshape(7, 2)
print(price_2d)


# %%
# B. Indexing & Slicing Array
# get the first 4 elements of the stock_price array

first_4_price = stock_price[:4]
print(first_4_price)


# %%
# get the price from the second rows and first column of the price_2d

second_row_first_column = price_2d[1:0]
print(second_row_first_column)


# %%
# C. Reshaping Array
# Reshape the price_2d array to a 1-dimentional array

price_1d = price_2d.reshape(14,)
print(price_1d)


# %%
# D. stacking Array
# vertically stack 2 arrays

vertical_stack = np.vstack((stock_price, price_1d))
print(vertical_stack)


# %%
# E. Broadcastind Array
# subtract 5 from every element in the stock_price array

stock_price_minus_5 = stock_price - 5.0
print(stock_price_minus_5)