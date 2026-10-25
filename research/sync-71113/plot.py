#!/usr/bin/env python3
"""Render the manuscript's correlation figure; optional Matplotlib dependency."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader((ROOT / "correlations.csv").open()))
lag = [int(row["lag"]) for row in rows]
series = [
    ("nested_7_11_13_aperiodic", "Nested 7 × 11 × 13 · aperiodic", "#176b91", 143),
    ("crt_product_aperiodic", "CRT ordering · aperiodic", "#a15d22", 122),
    ("crt_product_periodic", "CRT ordering · periodic", "#6b5195", 143),
]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                     "svg.hashsalt": "SYNC-71113-001-v1"})
fig, axes = plt.subplots(2, 3, figsize=(11.8, 5.7), sharex=True)
for col, (key, title, color, peak) in enumerate(series):
    values = [int(row[key]) / 1001 for row in rows]
    for row in (0, 1):
        ax = axes[row, col]
        ax.axhline(0, color="#9aa3aa", linewidth=0.5)
        # One segmented path keeps the exported vector figure compact.
        stem_x = [v for k in lag for v in (k, k, float("nan"))]
        stem_y = [v for y in values for v in (0, y, float("nan"))]
        ax.plot(stem_x, stem_y, color=color, linewidth=0.6)
        ax.set_xlim(-12, 1012)
        ax.set_xticks([0, 250, 500, 750, 1000])
        ax.grid(axis="y", alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
        if row == 0:
            ax.set_ylim(-0.19, 1.06)
            ax.set_title(title, fontsize=10, pad=11)
        else:
            ax.set_ylim(-0.16, 0.16)
            ax.axhline(peak / 1001, color=color, linestyle="--", linewidth=0.6, alpha=0.6)
            ax.axhline(-peak / 1001, color=color, linestyle="--", linewidth=0.6, alpha=0.6)
            ax.set_xlabel("Lag (samples)")
            ax.text(0.98, 0.94, f"Peak off-peak magnitude: {peak}/1001",
                    transform=ax.transAxes, ha="right", va="top", fontsize=8,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
axes[0, 0].set_ylabel("Correlation / 1001")
axes[1, 0].set_ylabel("Off-peak detail")
fig.suptitle("Ordering and boundary convention change the correlation", fontsize=14, y=0.99)
fig.text(0.5, 0.015, "Exact finite signals; these plots do not measure detection performance in noise.",
         ha="center", fontsize=9, color="#46515b")
fig.tight_layout(rect=(0, 0.05, 1, 0.96))
fig.savefig(ROOT / "autocorrelation.svg", metadata={"Date": "2026-10-25"})
fig.savefig(ROOT / "autocorrelation-preview.png", dpi=150)
print(ROOT / "autocorrelation.svg")
