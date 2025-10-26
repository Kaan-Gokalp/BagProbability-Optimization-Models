import numpy as np
import matplotlib.pyplot as plt

# Parameters
m, T, k = 15, 30, 3

def feasible_configs(m, T, k):
    """Generate all integer feasible (b_i, x_i) configurations."""
    results = []
    for b in itertools.product(range(1, m), repeat=k):
        if sum(b) != m:
            continue
        for x in itertools.product(range(1, T), repeat=k):
            if sum(x) != T or any(b[i] > x[i] for i in range(k)):
                continue
            P = np.prod([b[i] / x[i] for i in range(k)])
            results.append((b, x, P))
    return results

configs = feasible_configs(m, T, k)
P_values = [c[2] for c in configs]
maxP = max(P_values)
best = [c for c in configs if abs(c[2] - maxP) < 1e-6]

print("Optimum P =", round(maxP, 4))
for b, x, P in best:
    print("b =", b, "x =", x, "P =", round(P, 4))

# --- Visualization ---
# 2D heatmap: aggregate P by one ratio (e.g., b1/x1 vs b2/x2)
ratios = np.array([[c[0][0]/c[1][0], c[0][1]/c[1][1], c[2]] for c in configs])
r1, r2, P_vals = ratios[:,0], ratios[:,1], ratios[:,2]

plt.figure(figsize=(7,6))
plt.scatter(r1, r2, c=P_vals, cmap="viridis", s=30, edgecolors="k")
plt.colorbar(label="Success Probability (P)")
plt.xlabel("b₁/x₁")
plt.ylabel("b₂/x₂")
plt.title("Figure S1. Heatmap of P values for k=3 (m=15, T=30)")
plt.grid(True)
plt.tight_layout()
plt.savefig('supp_mat1.png', dpi=300)
plt.show()
