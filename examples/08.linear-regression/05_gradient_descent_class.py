import numpy as np

class MultipleLinearRegression:
    def __init__(self, learning_rate=0.001, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        print(f"n_samples {n_samples}, n_features{n_features}")
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iterations):
            # Predictions
            y_pred = np.dot(X, self.w) + self.b

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update weights and bias
            """print("dw", dw)
            print("dw.shape", dw.shape)
            print("db", db)
            print("weights", self.w) """
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.w) + self.b


# Example usage:
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([6, 10, 12, 23])
model = MultipleLinearRegression()
model.fit(X_train, y_train)

print("w :", model.w)
print("b :", model.b)

X_test = np.array([[5, 6], [6, 7]])
y_pred = model.predict(X_test)
print("X_test:", X_test)
print("y_pred:", y_pred)