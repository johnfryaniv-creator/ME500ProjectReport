"""Fig. 1: steady-state amplitude ratio A(x) along the Kelvin-Voigt rod.

Python version of fig:amp in project/sections/08_illustration.tex.
A(x) comes from eq:amplitude, with alpha and beta from eq:alpha_beta.
As a check, it is also computed directly from the complex solution
|sin(k(L-x)) / sin(kL)| (eq:X_solution) with k = beta - i*alpha.
"""
import matplotlib.pyplot as plt
import numpy as np

from style import SINGLE_COL, apply_style, save_fig

OMEGA_L_OVER_C = 7.0              # nondimensional drive frequency, omega*L/c
OMEGA_TAU = [0.0, 0.05, 0.2, 1.0]  # nondimensional damping, omega*tau


def wavenumbers(omega_tau, omega_l_over_c=OMEGA_L_OVER_C):
    """Return (beta*L, alpha*L) from eq:alpha_beta."""
    r = np.sqrt(1.0 + omega_tau**2)
    beta_l = omega_l_over_c / r * np.sqrt((r + 1.0) / 2.0)
    alpha_l = omega_l_over_c / r * np.sqrt((r - 1.0) / 2.0)
    return beta_l, alpha_l


def amplitude_closed_form(xi, beta_l, alpha_l):
    """Amplitude ratio A at xi = x/L, eq:amplitude."""
    num = np.cosh(2 * alpha_l * (1 - xi)) - np.cos(2 * beta_l * (1 - xi))
    den = np.cosh(2 * alpha_l) - np.cos(2 * beta_l)
    return np.sqrt(num / den)


def amplitude_complex(xi, beta_l, alpha_l):
    """Amplitude ratio A at xi = x/L, from |sin(k(L-x))/sin(kL)|."""
    k_l = beta_l - 1j * alpha_l
    return np.abs(np.sin(k_l * (1 - xi)) / np.sin(k_l))


def main():
    apply_style()
    xi = np.linspace(0.0, 1.0, 1001)

    fig, ax = plt.subplots(figsize=(SINGLE_COL, 2.4))

    print(f"Amplitude ratio A(x), omega*L/c = {OMEGA_L_OVER_C}")
    print(f"{'omega*tau':>9} {'beta*L':>8} {'alpha*L':>8} {'A(0)':>6} {'A(L)':>6}"
          f" {'max A':>6} {'at x/L':>6} {'min A, x/L<0.95':>16} {'|closed-complex|':>16}")
    for wt in OMEGA_TAU:
        beta_l, alpha_l = wavenumbers(wt)
        amp = amplitude_closed_form(xi, beta_l, alpha_l)
        err = np.max(np.abs(amp - amplitude_complex(xi, beta_l, alpha_l)))
        interior = xi < 0.95
        i_max = np.argmax(amp)
        print(f"{wt:9.2f} {beta_l:8.5f} {alpha_l:8.5f} {amp[0]:6.3f} {amp[-1]:6.3f}"
              f" {amp[i_max]:6.3f} {xi[i_max]:6.3f} {amp[interior].min():16.4f} {err:16.2e}")

        label = r"$\omega\tau = 0$ (elastic)" if wt == 0 else rf"$\omega\tau = {wt:g}$"
        ax.plot(xi, amp, label=label)

    ax.set_xlabel(r"Position along rod, $x/L$ (–)")
    ax.set_ylabel(r"Amplitude ratio, $\mathcal{A} = |u|_{\max}/U_0$ (–)")
    ax.set_xlim(0, 1)
    ax.set_ylim(bottom=0)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2,
              handlelength=1.5, columnspacing=1.5)

    save_fig(fig, "fig1_amplitude")


if __name__ == "__main__":
    main()
