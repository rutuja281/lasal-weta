from __future__ import annotations

from pathlib import Path
import os

import matplotlib.pyplot as plt

REPORT_MONTH = os.environ.get("REPORT_MONTH", "Dec2025")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"
TABS = ROOT / "tables"
FIGS.mkdir(exist_ok=True)
TABS.mkdir(exist_ok=True)


def savefig(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()


def build_operating_schedule() -> None:
    # TODO: read schedule source data from DATA and plot.
    plt.figure()
    plt.title("Operating schedule (placeholder)")
    savefig(FIGS / f"{REPORT_MONTH}_OperatingSchedule_Report.png")


def build_precip_summary() -> None:
    # TODO: read station precip data from DATA and plot.
    plt.figure()
    plt.title("Precip summary (placeholder)")
    savefig(FIGS / f"{REPORT_MONTH}_PrecipSummary_Report.png")


def build_historical_baseline() -> None:
    # TODO: plot historical baseline comparisons.
    plt.figure()
    plt.title("Historical baseline (placeholder)")
    savefig(FIGS / f"{REPORT_MONTH}_HistoricalBaseline_Report.png")


def build_radiometer_vilw_diff() -> None:
    # TODO: radiometer processing plot.
    plt.figure()
    plt.title("Radiometer VILW diff (placeholder)")
    savefig(FIGS / f"Radiometer_VILWDiff_{REPORT_MONTH}.png")


def build_tables() -> None:
    out = TABS / "data_timestamp.tex"
    out.write_text(f"Data updated for {REPORT_MONTH}\n")


def main() -> None:
    build_operating_schedule()
    build_precip_summary()
    build_historical_baseline()
    build_radiometer_vilw_diff()
    build_tables()
    print("Done.")


if __name__ == "__main__":
    main()
