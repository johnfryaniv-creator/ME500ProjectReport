# ME500 Project Report

LaTeX report (`project/`) on the steady-state harmonic response of a Kelvin–Voigt rod,
plus Python scripts that generate its figures.

## Rules for Claude

- Do **not** modify anything under `project/` except `project/figures/`, which holds generated figures.
  The `.tex` files are edited by the two authors; suggest LaTeX changes (e.g. `\includegraphics` lines) in chat instead.

## Python stack

- Dependencies are in `requirements.txt` (numpy, pandas, matplotlib, seaborn, scipy), installed by the setup script.
  Install manually with `pip install -r requirements.txt`.

## Layout

- Raw data in `data/`. Processed data in `data/processed/`.
- One script per figure in `figscripts/`, e.g. `figscripts/fig1_amplitude.py`.
  Run from the repo root: `python figscripts/fig1_amplitude.py`.
- Save outputs to `project/figures/` as PNG (300 dpi), using `save_fig()` from `figscripts/style.py`.
  In LaTeX they are referenced as `\includegraphics{figures/<name>.png}` (paths are relative to `project/main.tex`).

## Figure style

- Use `figscripts/style.py` (`apply_style()`) in every figure script.
- Single-column width 3.5 in (`SINGLE_COL`), double-column 7 in (`DOUBLE_COL`).
- Sans-serif font, 8 pt axis labels, 7 pt ticks.
- Colorblind-safe palette (Okabe-Ito, `OKABE_ITO` / default color cycle).
- Label axes with units (use `(–)` for dimensionless quantities). No titles; captions go in the paper.
- After generating a figure, view the PNG and check it before reporting done.
- Print a summary of the plotted data so results can be sanity-checked.
