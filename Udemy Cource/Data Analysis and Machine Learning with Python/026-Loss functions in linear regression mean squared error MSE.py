# %%
import numpy as np
import matplotlib.pyplot as plt

def mse_loss(y_true, y_pred):
    squared_difference = (y_true - y_pred) ** 2
    sum_squared_difference = np.sum(squared_difference)

    n = len(y_true)
    mse_loss = (1 / n) * sum_squared_difference
    return mse_loss


# %%
y_true = np.array([1, 2, 3])
y_pred = np.array([1.5, 2.5, 2.9])
mse = mse_loss(y_true, y_pred)

print(f"MSE Loss : {mse}")


# %%
plt.plot(y_true, "bo", label= "True Variable")
plt.plot(y_pred, "r-.", label= "Prediction")

plt.legend()
plt.show()