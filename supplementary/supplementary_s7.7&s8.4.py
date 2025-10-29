# Code: Projected Hessian eigenvalues (S7.7) and numerical table (S8.4)
import numpy as np
from math import exp
import matplotlib.pyplot as plt
import csv

# --- utility: partitions of n into k positive integers ---
def partitions_of_n_into_k(n, k):
    if k == 1:
        yield (n,)
    else:
        for i in range(1, n - k + 2):
            for tail in partitions_of_n_into_k(n - i, k - 1):
                yield (i,) + tail

# --- Projected Hessian eigenvalues (S7.7) ---
def projected_hessian_eigenvalues(k, m, T):
    b_star, x_star = m / k, T / k
    H_bb = -np.eye(k) / (b_star**2)
    H_xx =  np.eye(k) / (x_star**2)
    H = np.block([[H_bb, np.zeros((k,k))],
                  [np.zeros((k,k)), H_xx]])
    def basis_minus_one(k):
        B = np.zeros((k, k-1))
        for i in range(k-1):
            B[i, i] = 1
            B[i+1, i] = -1
        return B
    Qb = basis_minus_one(k)
    Qx = basis_minus_one(k)
    Q = np.block([[Qb, np.zeros_like(Qb)], [np.zeros_like(Qx), Qx]])
    H_proj = Q.T @ H @ Q
    eigvals = np.linalg.eigvals(H_proj)
    eigvals_sorted = np.sort(eigvals)
    return eigvals_sorted.real, H_proj

# --- brute force best discrete search (small sizes only) ---
def best_discrete_product(k, m, T):
    best = 0.0
    best_configs = []
    bs = list(partitions_of_n_into_k(m, k))
    xs = list(partitions_of_n_into_k(T, k))
    for b in bs:
        for x in xs:
            ok = True
            for i in range(k):
                if not (0 < b[i] < x[i]):
                    ok = False
                    break
            if not ok:
                continue
            P = 1.0
            for i in range(k):
                P *= b[i] / x[i]
            if P > best + 1e-12:
                best = P
                best_configs = [(b, x, P)]
            elif abs(P - best) <= 1e-12:
                best_configs.append((b, x, P))
    return best, best_configs

# --- run S7.7 examples ---
examples_b6 = [(3, 9, 30), (3, 15, 30)]
for k, m, T in examples_b6:
    eigvals, Hproj = projected_hessian_eigenvalues(k, m, T)
    print(f"k={k}, m={m}, T={T}: eigenvalues = {np.round(eigvals,6)}")

# --- run S8.4 examples and build table ---
example_table = [(3,9,30), (3,15,30), (4,12,24)]
rows = []
for (k, m, T) in example_table:
    P_cont = (m / T) ** k
    best_P, best_configs = best_discrete_product(k, m, T)
    bound = exp((k / 2.0) * (1.0 / m + 1.0 / T))
    rep = best_configs[0] if best_configs else None
    rows.append((k, m, T, P_cont, best_P, bound, rep))

# Save CSV
with open('s8.4_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['k','m','T','P_cont','P_disc_best','bound_factor','best_b','best_x','best_P'])
    for k,m,T,Pcont,Pdisc,bnd,rep in rows:
        if rep is None:
            writer.writerow([k,m,T,Pcont,Pdisc,bnd,'','',''])
        else:
            b,x,P = rep
            writer.writerow([k,m,T,Pcont,Pdisc,bnd,str(b),str(x),P])

# --- produce figure for k=3,m=9,T=30 ---
k,m,T = 3,9,30
best, configs = best_discrete_product(k,m,T)
vals = []
for b,x,P in configs:
    r1 = b[0]/x[0]
    r2 = b[1]/x[1]
    vals.append((r1, r2, P))
vals = np.array(vals)
plt.figure(figsize=(6,5))
plt.scatter(vals[:,0], vals[:,1], c=vals[:,2], cmap='viridis', s=40, edgecolor='k')
plt.colorbar(label='P (success probability)')
plt.xlabel('b1/x1')
plt.ylabel('b2/x2')
plt.title(f'Figure S2: k={k}, m={m}, T={T} — P values')
plt.tight_layout()
plt.savefig('figure_S1_k3_m9_T30.png', dpi=300)
plt.close()

