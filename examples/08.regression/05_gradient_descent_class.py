import numpy as np

class MultipleLinearRegression:
    def __init__(self, learning_rate=0.001, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        print("n_samples, n_features", n_samples, n_features)
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            # Predictions
            y_pred = np.dot(X, self.weights) + self.bias

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update weights and bias
            print("dw", dw)
            print("dw.shape", dw.shape)
            print("db", db)
            print("weights", self.weights)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Example usage:
#X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
#y_train = np.array([5, 7, 9, 11])
X_train = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]).reshape(-1,1)
y_train = np.array([5, 8, 16, 19, 30, 35, 30, 43, 41, 44, 39])
model = MultipleLinearRegression()
model.fit(X_train, y_train)

print("model.weights : ", model.weights)
print("model.bias : ", model.bias)

#X_test = np.array([[5, 6], [6, 7]])
X_test = np.array([28, 53]).reshape(-1,1)
predictions = model.predict(X_test)
print(predictions)