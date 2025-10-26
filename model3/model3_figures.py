# Model 3 - Exhaustive first-scan simulation (k = 3)
# Gereksinimler: numpy, pandas, matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parametreler
m = 15   # toplam beyaz top
T = 30   # toplam top
k = 3    # kutu sayısı (bu script k=3 için exhaustive tarama yapar)

records = []
# x1,x2,x3 >=1 ve x1+x2+x3 = T (k=3 için)
for x1 in range(1, T-1):
    for x2 in range(1, T-x1):
        x3 = T - x1 - x2
        # b_i için alt-üst sınırlar (0 <= b_i <= x_i) ve sum(b)=m
        b1_min = max(0, m - (x2 + x3))
        b1_max = min(x1, m)
        for b1 in range(b1_min, b1_max + 1):
            b2_min = max(0, m - b1 - x3)
            b2_max = min(x2, m - b1)
            for b2 in range(b2_min, b2_max + 1):
                b3 = m - b1 - b2
                if 0 <= b3 <= x3:
                    r1 = b1 / x1
                    r2 = b2 / x2
                    r3 = b3 / x3
                    P = float(r1 * r2 * r3)
                    any_b_eq0 = (b1 == 0) or (b2 == 0) or (b3 == 0)
                    any_b_eq_x = (b1 == x1) or (b2 == x2) or (b3 == x3)
                    interior = (0 < b1 < x1) and (0 < b2 < x2) and (0 < b3 < x3)
                    ratio_mean = np.mean([r1, r2, r3])
                    ratio_std = np.std([r1, r2, r3])
                    records.append((x1,x2,x3,b1,b2,b3,r1,r2,r3,ratio_mean,ratio_std,P,interior,any_b_eq_x,any_b_eq0))

cols = ["x1","x2","x3","b1","b2","b3","r1","r2","r3","ratio_mean","ratio_std","P","interior","any_b_eq_x","any_b_eq0"]
df = pd.DataFrame(records, columns=cols)

# Özet istatistikler
summary = {
    "total_configurations": len(df),
    "P_min": df["P"].min(),
    "P_max": df["P"].max(),
    "P_mean": df["P"].mean(),
    "P_median": df["P"].median()
}
print("Summary:", summary)

# En iyi konfigürasyonlar
top20 = df.sort_values("P", ascending=False).head(20)
print("\nTop 20 (highest P) values:")
print(top20[["b1","b2","b3","x1","x2","x3","r1","r2","r3","P","interior","any_b_eq_x"]].to_string(index=False))

# Plot 1: Histogram of P
plt.figure(figsize=(8,6))
plt.hist(df["P"], bins=60)
plt.xlabel("Success Function (P)")
plt.ylabel("Frequency")
plt.title(f"Model 3: Distribution of the Success Function (m={m}, T={T}, k={k})")
plt.savefig('model3_histogram.png', dpi=300)
plt.show()

# Plot 2: ratio stddev vs P (AM-GM'ye dair görsel kanıt)
plt.figure(figsize=(8,6))
plt.scatter(df["ratio_std"], df["P"], s=8)
plt.xlabel("Ratios StdDev (std of b_i/x_i)")
plt.ylabel("Success Function (P)")
plt.title("Model 3: Ratio StdDev vs P (lower std => higher probability of P)")
plt.savefig('model3_stddev.png', dpi=300)
plt.show()

# Plot 3: interior vs boundary counts
counts = df["interior"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(["interior", "boundary"], [counts.get(True,0), counts.get(False,0)])
plt.ylabel("Number of Configurations")
plt.title("Interior vs Boundary Configuration Numbers")
plt.savefig('model3_configuration.png', dpi=300)
plt.show()
