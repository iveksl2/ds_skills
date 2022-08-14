# https://www.youtube.com/watch?v=PxV-l5BMfrY

import numpy as np 
import matplotlib.pyplot as plt

X = [0]

for i in range(1000):
    X.append(np.random.randn() + X[-1]*0.9) # more trending

plt.plot(np.cumsum(X)); plt.show()

plt.plot(X[:-1], X[1:],'o'); plt.show()

for i in range(1000):
    X.append(np.random.randn() - X[-1]*0.9) # more mean reverting

plt.plot(np.cumsum(X)); plt.show()

plt.plot(X[:-1], X[1:],'o'); plt.show()

X = [0,0]
for i in range(1000):
    X.append(np.random.randn() + X[-1]*0.1 + X[-2]*.5) # more mean reverting

plt.plot(np.cumsum(X)); plt.show()

plt.plot(X[:-2], X[2:],'o'); plt.show()
