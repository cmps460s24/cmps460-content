# Gradient Descent for Linear Regression
# yhat = wx + b 
# mse = (y-yhat)**2 / N 
import numpy as np

np.set_printoptions(suppress = True,
   formatter = {'float_kind':'{:f}'.format})

# Initialise some parameters
X = np.random.randn(10,1)
y = 5*X + np.random.rand()

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([5, 7, 9, 11])

print(X.shape, y.shape)

n_features = X.shape[1]
# Parameters
w = np.zeros(n_features)
b = 0
# Hyperparameter 
learning_rate = 0.001


def yhat(x, w, b):
    return w*x + b

# Create gradient descent function
def descend(X, y, w, b, learning_rate): 
    m = X.shape[0]
    y_pred = np.dot(X, w) + b
    #print ("y_pred", y_pred)

    # Compute gradients
    dw = (1/m) * np.dot(X.T, (y_pred-y))
    print ("dw", dw)
    db = (1/m) * np.sum(y_pred-y)
    print ("db", db)

    # Make an update to the w parameter 
    w = w - (learning_rate * dw)
    b = b - (learning_rate * db)
    return w, b 

# Iteratively make updates
for epoch in range(1000): 
    w, b = descend(X, y, w, b, learning_rate)
    y_pred = np.dot(X, w) + b

    #print("y_pred-y", y_pred-y)
    mse = np.mean((y_pred-y)**2)
    print(f'{epoch} mse is {mse}, paramters w:{w}, b:{b}')
