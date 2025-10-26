import numpy as np
import matplotlib.pyplot as plt

def water_filling(x, m):
    """Water-filling algorithm for concave log(b_i) maximization."""
    x = np.array(sorted(x))  # Sort capacities
    n = len(x)
    remaining = m
    S = np.arange(n)
    b = np.zeros(n)

    while len(S) > 0:
        lam = remaining / len(S)
        if np.all(x[S] >= lam):
            b[S] = lam
            break
        else:
            full = S[x[S] < lam]
            b[full] = x[full]
            remaining -= np.sum(x[full])
            S = S[x[S] >= lam]

    return b, lam

# Example parameters
x = np.array([3, 5, 8, 10])
m = 18

b, lam = water_filling(x, m)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(range(len(x)), x, color="#d0d0d0", label="Capacity x_i")
plt.bar(range(len(x)), b, color="#4a90e2", label="Filled level b_i")
plt.axhline(y=lam, color="red", linestyle="--", label=f"Water level λ = {lam:.2f}")

plt.xticks(range(len(x)), [f"i={i+1}" for i in range(len(x))])
plt.xlabel("Buckets (i)")
plt.ylabel("Amount")
plt.title("Water-Filling Algorithm Visualization")
plt.legend()
plt.tight_layout()
plt.savefig("model3_waterfilling.png", dpi=300)
plt.show()

print("Optimal distribution b* =", np.round(b, 3))
print("Total =", np.sum(b))