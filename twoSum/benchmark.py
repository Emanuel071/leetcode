#!/usr/bin/env python3
"""Benchmark and plot runtime scaling for two-sum implementations.

This script times the provided `Solution.twoSum` implementation (from
`twoSum_optimized.py`) and a naive O(n^2) implementation (for comparison).
It prints timing tables and, if matplotlib/numpy are installed, saves a plot.
"""
from __future__ import annotations

import random
import statistics
from time import perf_counter
from typing import Callable, List, Tuple, Dict

try:
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MPL = True
except Exception:
    HAS_MPL = False

from twoSum_optimized import Solution


def generate_no_solution(n: int) -> Tuple[List[int], int]:
    """Return a list of positive ints and a target that guarantees no solution.

    Using a negative target while numbers are positive ensures the fast
    implementation will fully scan the list (no early exit).
    """
    nums = list(range(1, n + 1))
    random.shuffle(nums)
    return nums, -1


def naive_two_sum(nums: List[int], target: int) -> List[int]:
    """Naive O(n^2) two-sum for comparison."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def time_func(func: Callable[[List[int], int], List[int]], nums: List[int], target: int, trials: int = 3) -> Tuple[float, float]:
    times: List[float] = []
    # run a few trials and return mean and stdev
    for _ in range(trials):
        t0 = perf_counter()
        func(nums, target)
        t1 = perf_counter()
        times.append(t1 - t0)
    mean = statistics.mean(times)
    stdev = statistics.stdev(times) if len(times) > 1 else 0.0
    return mean, stdev


def benchmark(trials: int = 3) -> Dict[str, List[Tuple[int, float, float]]]:
    """Run benchmarks for the fast and naive implementations.

    For practical runtimes, we use larger sizes for the fast algorithm and
    much smaller sizes for the naive one.
    """
    sol = Solution()

    sizes_fast = [2000, 4000, 8000, 16000]
    sizes_naive = [100, 200, 400, 800]

    results: Dict[str, List[Tuple[int, float, float]]] = {"Solution.twoSum": [], "naive": []}

    print("Benchmarking Solution.twoSum (no-solution inputs to force full scan)")
    for n in sizes_fast:
        nums, target = generate_no_solution(n)
        mean, stdev = time_func(sol.twoSum, nums, target, trials=trials)
        results["Solution.twoSum"].append((n, mean, stdev))
        print(f"  n={n:6d} mean={mean:.6e} std={stdev:.6e}")

    print("\nBenchmarking naive O(n^2) implementation")
    for n in sizes_naive:
        nums, target = generate_no_solution(n)
        mean, stdev = time_func(naive_two_sum, nums, target, trials=trials)
        results["naive"].append((n, mean, stdev))
        print(f"  n={n:6d} mean={mean:.6e} std={stdev:.6e}")

    return results


def plot_results(results: Dict[str, List[Tuple[int, float, float]]], out_file: str = "runtime.png") -> None:
    if not HAS_MPL:
        print("matplotlib/numpy not available; skipping plot. Install with: pip install matplotlib numpy")
        return

    plt.figure(figsize=(8, 5))
    # Plot each dataset with error bars
    for name, data in results.items():
        ns = [n for n, _, _ in data]
        times = [t for _, t, _ in data]
        stdev = [s for _, _, s in data]
        plt.errorbar(ns, times, yerr=stdev, marker="o", label=name)

    # Add reference linear/quadratic curves using the first fast point as anchor
    if results["Solution.twoSum"]:
        n0, t0, _ = results["Solution.twoSum"][0]
        ns_lin = sorted(set(ns for name in results for ns, _, _ in results[name]))
        linear = [t0 * (n / n0) for n in ns_lin]
        quad = [t0 * (n / n0) ** 2 for n in ns_lin]
        plt.plot(ns_lin, linear, "--", label="linear reference")
        plt.plot(ns_lin, quad, "--", label="quadratic reference")

    plt.xlabel("n (array size)")
    plt.ylabel("time (seconds)")
    plt.title("Two-Sum runtime scaling")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_file)
    print(f"Saved plot to {out_file}")


if __name__ == "__main__":
    # small number of trials to keep runtime reasonable
    results = benchmark(trials=3)
    if HAS_MPL:
        plot_results(results, out_file="two_sum_runtime.png")
    else:
        print("Install matplotlib and numpy to get a plot: pip install matplotlib numpy")
