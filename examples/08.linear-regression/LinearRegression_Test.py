import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

""" X = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 28, 53]).reshape(-1,1)
y = np.array([3, 8, 16, 19, 30, 35, 30, 43, 41, 44, 39, 35, 60])

X_train = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]).reshape(-1,1)
y_train = np.array([3, 8, 16, 19, 30, 35, 30, 43, 41, 44, 39])
X_test = np.array([28, 53]).reshape(-1,1)
y_test = np.array([35, 60])  """

print("X", X)
print("y", y)

fig = plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], y, color = "b", marker = "o", s = 30)
plt.show()

reg = LinearRegression(lr=0.01)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print("y_pred", y_pred)


def mse(y_test, y_pred):
    return np.mean((y_test - y_pred)**2)

mse = mse(y_test, y_pred)
print("MSE: ", mse)
print("Weights: ", reg.weights)
print("Bias: ", reg.bias)

y_pred_line = reg.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.show()