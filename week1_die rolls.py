import matplotlib.pyplot as plt
import numpy as np
n_rolls = 100000
counts = []
for i in range(n_rolls):
    rolls = np.random.randint(1, 7, 2)
    sum = rolls.sum()
    counts.append(sum)
plt.hist(counts, density = True)
plt.xlabel('sum')
plt.ylabel('frequency')
plt.show()