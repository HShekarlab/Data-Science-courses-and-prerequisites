# %%
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

x_1 = np.random.uniform(low= 0, high= 10, size= 50)
x_2 = np.random.normal(loc= 5, scale= 2, size= 50)

x = np.c_[x_1, x_2]

y = (2 * x_1) - (3 * x_2) + 1 + np.random.normal(loc= 5, scale= 2, size= 50)


# %%
fig = px.scatter_3d(x= x_1, y= x_2, z= y,
                    labels= {"x": "x_1", "y": "x_2", "z": "y"},
                    title= "3D Scatter Plot of x_1, x_2 & y")

fig.show()


# %%
x_bias = np.c_[np.ones((len(x), 1)), x]


# %%
w = np.random.normal(loc= 0, scale= 0.5, size= x_bias.shape[1])


# %%
num_epochs = 100
learning_rate = 0.01
losses = []
gradients = []
prev_loss = np.inf
epoch = 0


# %%
while True:
    y_pred = x_bias.dot(w)

    mse_loss = (1 / len(x)) * np.sum((y - y_pred) ** 2)
    losses.append(mse_loss)

    if np.abs(prev_loss - mse_loss) < 1e-8:
        break
    prev_loss = mse_loss

    w_grad = - (2 / len(x)) * x_bias.T.dot(y - y_pred)
    gradients.append(np.linalg.norm(w_grad))

    if np.linalg.norm(w_grad) < 1e-8:
        break

    w -= learning_rate * w_grad
    epoch += 1
    print(f"Epoch : {epoch}")


# %%
plt.plot(losses, color= "c")

plt.xlabel("Epoch")
plt.ylabel("Loss")


# %%
plt.plot(gradients, color= "deeppink")

plt.xlabel("Epoch")
plt.ylabel("Gradient")


# %%
print(f"Coefficients: {w[1:]}")
print(f"Intercept: {w[0]}")