import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.cos(x) 

plt.plot(x, y)
plt.title('Graph of cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
