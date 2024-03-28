# Gradient Descent for Linear Regression
# yhat = wx + b 
# mse = (y-yhat)**2 / N 
import numpy as np

np.set_printoptions(suppress = True,
   formatter = {'float_kind':'{:f}'.format})

# Initialise some parameters
X = np.random.randn(10,1)
y = 5*X + np.random.rand()

X = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]).reshape(-1,1)
y = np.array([5, 8, 16, 19, 30, 35, 30, 43, 41, 44, 39])

print(X.shape, y.shape)

# Parameters
w = 0.0 
b = 0.0 
# Hyperparameter 
learning_rate = 0.001


def yhat(x, w, b):
    return w*x + b

# Create gradient descent function
def descend(X, y, w, b, learning_rate): 
    dw = 0.0 
    db = 0.0 
    m = X.shape[0]
    # mse = (y-(wx+b)))**2

    # Predictions
    #y_pred = (X * w) + b
    y_pred = np.dot(X, w) + b
    print ("y_pred", y_pred)


    # Compute gradients
    dw = (1/m) * np.dot(X.T, (y_pred-y))
    print ("dw", dw)
    db = (1/m) * np.sum(y_pred-y)
    print ("db", db)

    """for xi, yi in zip(x,y): 
       dw += (yhat(xi, w, b) - yi) * xi
       db += yhat(xi, w, b) - yi

    dw = dw / m
    db = db / m """

    # Make an update to the w parameter 
    w = w - (learning_rate * dw)
    b = b - (learning_rate * db)
    return w, b 

# Iteratively make updates
m = X.shape[0]
for epoch in range(1000): 
    w, b = descend(X, y, w, b, learning_rate)
    #y_pred = (w*X) + b
    y_pred = np.dot(X, w) + b
    #print(w)
    #print(b)
    print("y_pred-y", y_pred-y)
    mse = np.mean((y_pred-y)**2)
    print(f'{epoch} mse is {mse}, paramters w:{w}, b:{b}')
    
#print(X,y)