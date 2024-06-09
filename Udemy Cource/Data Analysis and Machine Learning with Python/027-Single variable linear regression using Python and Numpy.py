# %%
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.random.uniform(low= 0, high= 10, size= 40)
y = (3 * x) + 7 + np.random.normal(loc= 0, scale= 2, size= 40)


# %%
plt.scatter(x, y, color= "b")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()


# %%
x_bias = np.c_[np.ones((40, 1)), x]

w = np.random.normal(loc= 0, scale= 0.5, size= 2)

learning_rate = 0.01

losses = []
gradients = []

prev_loss = np.inf
epoch = 0


# %%
while True:
    y_pred = x_bias.dot(w)
    mse_loss = (1 / 40) * np.sum((y - y_pred) ** 2)

    if np.abs(prev_loss - mse_loss) < 1e-8:
        break
    prev_loss = mse_loss

    w_grad = - (2 / 40) * x_bias.T.dot(y - y_pred)
    gradients.append(np.linalg.norm(w_grad))

    if np.linalg.norm(w_grad) < 1e-8:
        break

    w -= learning_rate * w_grad
    epoch += 1


# %%
plt.plot(losses)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()


# %%
plt.plot(gradients, color= "lime")

plt.xlabel("Eploch")
plt.ylabel("Gradient")


# %%
plt.scatter(x, y, color= "g")
plt.plot(x, x_bias.dot(w), color= "m")

plt.xlabel("x")
plt.ylabel("y")


# %%
print(f"Coefficients: {w[1:]}")
print(f"Intercept: {w[0]}")