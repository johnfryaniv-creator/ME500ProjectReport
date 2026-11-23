"""Shared matplotlib style for ME500 report figures.

Call ``apply_style()`` at the top of every figure script, then save with
``save_fig(fig, "figN_name")`` so every PNG lands in project/figures/ at 300 dpi.
"""
from pathlib import Path

import matplotlib as mpl

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
FIG_DIR = REPO_ROOT / "project" / "figures"

# Figure widths in inches. (The report's article text width is 6.5 in, so a
# DOUBLE_COL figure is included with width=\textwidth and scales slightly.)
SINGLE_COL = 3.5
DOUBLE_COL = 7.0

DPI = 300

# Okabe-Ito colorblind-safe palette. Yellow is last because it is hard to see
# as a thin line on white.
OKABE_ITO = {
    "black": "#000000",
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "bluish_green": "#009E73",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish_purple": "#CC79A7",
    "yellow": "#F0E442",
}
PALETTE = list(OKABE_ITO.values())


def apply_style():
    """Set rcParams for publication figures (sans-serif, 8 pt labels, 7 pt ticks)."""
    mpl.rcParams.update({
        # Fonts
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
        "mathtext.fontset": "dejavusans",
        "font.size": 8,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "axes.titlesize": 8,  # titles are not used; captions go in the paper
        # Colors
        "axes.prop_cycle": mpl.cycler(color=PALETTE),
        # Lines and axes
        "lines.linewidth": 1.0,
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "axes.grid": False,
        "legend.frameon": False,
        # Output
        "figure.dpi": 150,
        "savefig.dpi": DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
    })


def save_fig(fig, name):
    """Save ``fig`` as project/figures/<name>.png at 300 dpi and return the path."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / f"{name}.png"
    fig.savefig(path, dpi=DPI)
    print(f"Saved {path.relative_to(REPO_ROOT)}")
    return path
