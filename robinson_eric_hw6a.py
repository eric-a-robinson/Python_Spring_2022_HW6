import numpy as np
from matplotlib import pyplot as plt
from robinson_eric_hw6b import f
from robinson_eric_hw6b import g
from robinson_eric_hw6b import h
from robinson_eric_hw6b import i

x_f = np.arange(10**3)
x_g = np.arange(10**3)
x_h = np.arange(10**2)
x_i = np.arange(10**2)

fig, axs = plt.subplots(2,2)
axs[0,0].plot(x_f, f(x_f), color="magenta")
axs[0,0].set_xscale("log")
axs[0,0].set_yscale("log")
axs[0,0].set(xlabel="x",ylabel=r"$x^2$−2x+1")

axs[0,1].plot(x_g, g(x_g), color="royalblue")
axs[0,1].set_xscale("log")
axs[0,1].yaxis.set_label_position("right")
axs[0,1].yaxis.tick_right()
axs[0,1].set(xlabel="x",ylabel="sin(x)+5")

axs[1,0].plot(x_h,h(x_h), color="tomato")
axs[1,0].set_yscale("log")
axs[1,0].set(xlabel="x",ylabel=r"ln(x+1)+$x^2$+x")

axs[1,1].plot(x_i,i(x_i), "g--")
axs[1,1].set_yscale("log")
axs[1,1].yaxis.set_label_position("right")
axs[1,1].yaxis.tick_right()
axs[1,1].set(xlabel="x",ylabel=r"cos(x)-5+$x^3$")

plt.savefig("erics_cool_graphs.png", dpi=300)