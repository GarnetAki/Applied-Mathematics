import matplotlib.pyplot as plt
import numpy as np

fig3 = plt.figure()
ax = fig3.add_subplot(projection='3d')

x, y = np.mgrid[-20:20:50j, -20:20:50j]

F3 = 3*x**2 + 4*y**2 + 4*x + 3*y - 12
ax.plot_wireframe(x, y, F3)

plt.show()