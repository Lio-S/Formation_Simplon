import matplotlib.pyplot as plt

# plt.plot([1, 0, 3, 2]) # ici x va donc valoir 0, 1, 2, 3

# x = [-3, -1, 2]
# y = [4, -4, -3]
# plt.plot(x,y)
# plt.grid()
# plt.show()

import numpy as np
x = np.linspace(-50, 50, 40)
# fig, ax = plt.subplots(figsize=(7, 5))
# ax.plot(x, x**2, "-+")
# ax.set(title="Parabole",
#        xlabel="axe x",
#        ylabel="axe y")

# # plt.show()
# fig.show()
# help(fig.suptitle)
fig, (ax0, ax1) = plt.subplots(nrows=2,
                            ncols=1,
                            figsize=(7, 7),
                            sharex=True)
ax0.plot(x, 1/x)
ax0.set(title="Hyperbole",
        ylabel="axe y")
ax0.set_ylim([-0.5, 0.25])

ax1.plot(x, 3*x)
ax1.set(title="Droite",
        xlabel="axe x",
        ylabel="axe y")
fig.suptitle(t="Affichage de deux figures");
fig.show()