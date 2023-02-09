import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)
y = 1/x

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("1/x")
plt.title("Graph of 1/x")
plt.grid(True)
plt.show()
