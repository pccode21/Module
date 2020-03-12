import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6)
y = x * x

plt.plot(x, y, marker='o')
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points', weight='heavy', color='y'
    #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.5)
    #arrowprops = dict(facecolor = "r", headlength = 10, headwidth = 30, width = 20)
    )
plt.show()
