import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return(x*x)

# np.arange(start, stop, step) # start inclusive, stop exclusive
X = np.arange(-100, 100, 0.1)
print(X)
y = [f(x) for x in X]

plt.figure(figsize=(7, 4))
plt.plot(X, y,  linewidth=2)
plt.xlabel(r"$x$")
plt.ylabel(r"$f\  (x)$")
plt.grid()
#plt.show()

current_pos = (-90, f(-90))
plt.plot(X, y)
plt.scatter(current_pos[0], current_pos[1], color = "red")
#plt.show()

def f_derivative(x):
    return 2*x

current_pos = (-90, f(-90))

learning_rate = 0.01
for i in range(300):
    new_x = current_pos[0] - learning_rate * f_derivative(current_pos[0])
    new_y = f(new_x)
    current_pos = (new_x, new_y)

    print("Iteration: ", i, "Decrease x by: ", learning_rate * f_derivative(current_pos[0]),
          "New x: ", new_x, "New y: ", new_y)
    
    plt.plot(X, y)
    plt.scatter(current_pos[0], current_pos[1], color = "red")
    plt.pause(0.001)
    plt.clf()

#plt.show()