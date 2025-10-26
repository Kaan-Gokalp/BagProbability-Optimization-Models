"""
heatmap_model3.py

Efficient exhaustive parametric sweep for Model 3 (k boxes).
Generates a heatmap of maximal P = prod_i (b_i / x_i) for grid of (k, m/T) pairs.

Usage:
    python heatmap_model3.py

Dependencies:
    numpy, matplotlib, optionally tqdm (for progress bar), multiprocessing standard lib.
"""

import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import argparse
import time
try:
    from tqdm import tqdm
    HAS_TQDM = True
except Exception:
    HAS_TQDM = False

# -------------------------
# Combinatorics helpers
# -------------------------
def partitions_positive(n, k):
    """Generate all k-tuples of positive integers summing to n."""
    if k == 1:
        yield (n,)
    else:
        # i ranges from 1 to n-(k-1)
        for i in range(1, n - k + 2):
            for tail in partitions_positive(n - i, k - 1):
                yield (i,) + tail

def compositions_nonneg(n, k):
    """Generate all k-tuples of nonnegative integers summing to n."""
    if k == 1:
        yield (n,)
    else:
        for i in range(0, n + 1):
            for tail in compositions_nonneg(n - i, k - 1):
                yield (i,) + tail

# -------------------------
# Core enumeration (single b)
# -------------------------
def evaluate_b_tuple_local(b, k, m, T):
    """Given fixed b tuple, enumerate feasible x and return best local configs."""
    x_min = [bi + 1 for bi in b]            # minimal x to ensure b_i < x_i
    s_min = sum(x_min)
    R = T - s_min
    best_local = 0.0
    best_local_list = []
    if R < 0:
        return best_local, best_local_list
    # enumerate extras (nonneg comps of R)
    for extra in compositions_nonneg(R, k):
        x = tuple(x_min[i] + extra[i] for i in range(k))
        # compute P
        P = 1.0
        for i in range(k):
            P *= b[i] / x[i]
        # update best
        if P > best_local + 1e-15:
            best_local = P
            best_local_list = [(b, x, P)]
        elif abs(P - best_local) <= 1e-15:
            best_local_list.append((b, x, P))
    return best_local, best_local_list

# Worker for multiprocessing
def worker_evaluate(args):
    return evaluate_b_tuple_local(*args)

# -------------------------
# High-level best search
# -------------------------
def best_P_for_params(k, m, T, nproc=1, show_progress=False):
    """Return best P and one list of best configs for given (k,m,T)."""
    bs = list(partitions_positive(m, k))
    best_all = 0.0
    best_configs_all = []

    if nproc > 1:
        # prepare args
        args = [(b, k, m, T) for b in bs]
        with Pool(processes=nproc) as pool:
            iterator = pool.imap_unordered(worker_evaluate, args)
            if show_progress and HAS_TQDM:
                iterator = tqdm(iterator, total=len(args), desc=f"k={k}, m={m}")
            for (best_local, best_local_list) in iterator:
                if best_local > best_all + 1e-15:
                    best_all = best_local
                    best_configs_all = best_local_list
                elif abs(best_local - best_all) <= 1e-15:
                    best_configs_all.extend(best_local_list)
    else:
        it = bs
        if show_progress and HAS_TQDM:
            it = tqdm(bs, desc=f"k={k}, m={m}")
        for b in it:
            best_local, best_local_list = evaluate_b_tuple_local(b, k, m, T)
            if best_local > best_all + 1e-15:
                best_all = best_local
                best_configs_all = best_local_list
            elif abs(best_local - best_all) <= 1e-15:
                best_configs_all.extend(best_local_list)
    return best_all, best_configs_all

# -------------------------
# Sweep and plotting
# -------------------------
def sweep_and_plot(ks, ratios, T, nproc=1, outpath='heatmap_model3.png'):
    """
    ks: list of k values
    ratios: list/array of m/T ratios (0<ratio<1)
    T: total number of balls
    nproc: processes to use
    """
    heat = np.zeros((len(ks), len(ratios)))
    runtime_stats = []

    total_tasks = len(ks) * len(ratios)
    start_all = time.time()
    idx = 0
    for i, k in enumerate(ks):
        for j, r in enumerate(ratios):
            idx += 1
            m = max(1, int(round(r * T)))
            # ensure feasibility bounds
            if m <= 0 or m >= T:
                heat[i, j] = np.nan
                continue
            t0 = time.time()
            bestp, bestconfigs = best_P_for_params(k, m, T, nproc=nproc, show_progress=False)
            t1 = time.time()
            heat[i, j] = bestp
            runtime_stats.append((k, m, T, t1 - t0, len(bestconfigs)))
            # optional: print progress every few
            if idx % 5 == 0:
                print(f"[{idx}/{total_tasks}] Completed k={k}, m={m}, T={T}, bestP={bestp:.6f}, time={t1 - t0:.1f}s")
    total_time = time.time() - start_all
    print(f"Total sweep runtime: {total_time:.1f}s")

    # Plot heatmap
    plt.figure(figsize=(9, 4.5))
    extent = [min(ratios), max(ratios), min(ks), max(ks)]
    # replace zeros with small eps for log color if desired; here color linear
    im = plt.imshow(heat, extent=extent, origin='lower', aspect='auto', cmap='inferno')
    plt.colorbar(im, label='Maximal P')
    plt.xlabel('m / T')
    plt.ylabel('k (number of boxes)')
    plt.title(f'Parametric heatmap: T={T}, nproc={nproc}')
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    plt.close()
    return heat, runtime_stats

# -------------------------
# Main CLI
# -------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate parametric heatmap for Model 3 (exhaustive).")
    parser.add_argument("--T", type=int, default=30, help="Total balls T (default 30)")
    parser.add_argument("--ks", type=str, default="2,3,4", help="Comma-separated k values (default '2,3,4')")
    parser.add_argument("--ratios", type=str, default="0.2:0.8:13", help="ratio start:stop:steps (default '0.2:0.8:13')")
    parser.add_argument("--nproc", type=int, default=1, help="Number of processes for parallel runs (default 1)")
    parser.add_argument("--out", type=str, default="heatmap_model3.png", help="Output figure filename")
    args = parser.parse_args()

    # parse ks
    ks = [int(x) for x in args.ks.split(',')]
    # parse ratios
    try:
        a, b, s = args.ratios.split(':')
        start, stop, steps = float(a), float(b), int(s)
        ratios = np.linspace(start, stop, steps)
    except Exception:
        ratios = np.array([float(x) for x in args.ratios.split(',')])

    print(f"Running sweep with ks={ks}, ratios={ratios}, T={args.T}, nproc={args.nproc}")
    heat, stats = sweep_and_plot(ks, ratios, args.T, nproc=args.nproc, outpath=args.out)
    print("Done. Figure saved to", args.out)
