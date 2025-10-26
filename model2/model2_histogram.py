import numpy as np
import matplotlib.pyplot as plt

m = 6
n = 4
T = m + n

Ps = []
configs = []
for b in range(1, m):
    x_min = b
    x_max = min(b + (T - m), T-1)
    for x in range(x_min, x_max + 1):
        if x == 0 or (T - x) == 0: continue
        P = (b / x) * ((m - b) / (T - x))
        Ps.append(P)
        configs.append((b, x, P))

Ps = np.array(Ps)
plt.figure(figsize=(7,4.5))
plt.hist(Ps, bins=12)
plt.xlabel('P values')
plt.ylabel('Frequency')
plt.title(f'Model 2 — Histogram of P over feasible (b,x) (m={m}, n={n})')
plt.tight_layout()
plt.savefig('model2_histogram.png', dpi=300)
plt.show()

configs_sorted = sorted(configs, key=lambda t: t[2], reverse=True)
for c in configs_sorted[:5]:
    print(c)
