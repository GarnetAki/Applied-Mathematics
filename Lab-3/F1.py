import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x, y = np.mgrid[-20:20:50j, -20:20:50j]

F1 = x**2 + 2*(y**2) - x*y - 8*y + 1
ax.plot_wireframe(x, y, F1)

plt.show()