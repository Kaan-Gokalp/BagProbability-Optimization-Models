import numpy as np
import matplotlib.pyplot as plt

# --- Model 1 boundary curves ---
b_vals = np.linspace(0.01, 4.99, 500)
f1 = (5 - b_vals) / (10 - b_vals)
f2 = b_vals / (b_vals + 5)

plt.figure(figsize=(7,4.5))
plt.plot(b_vals, f1, label=r'$f_1(b)=\dfrac{5-b}{10-b}\ (x=b)$')
plt.plot(b_vals, f2, label=r'$f_2(b)=\dfrac{b}{b+5}\ (x=b+5)$')
plt.xlabel('b (white balls in A)')
plt.ylabel('P (probability two whites)')
plt.title('Model 1 — Boundary curves (x=b and x=b+5)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('model1_boundary_curves.png', dpi=300)
plt.show()
