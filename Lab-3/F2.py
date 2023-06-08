import matplotlib.pyplot as plt
import numpy as np

fig2 = plt.figure()
ax = fig2.add_subplot(projection='3d')

x, y = np.mgrid[-20:20:50j, -20:20:50j]

F2 = x**2 + y**2 + 0.5*x*y + 3*x + 2*y
ax.plot_wireframe(x, y, F2)

plt.show()