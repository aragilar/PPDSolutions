import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "values.csv"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("save_file")
    args = parser.parse_args()

    γ_interp = []
    v_r_interp = []
    γ_unassist = []
    v_r_unassist = []
    with DATA_FILE.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["kind"] == "interp":
                γ_interp.append(float(row['γ']))
                v_r_interp.append(float(row['v_rin_on_c_s']))
            elif row["kind"] == "unassisted":
                γ_unassist.append(float(row['γ']))
                v_r_unassist.append(float(row['v_rin_on_c_s']))
            else:
                raise RuntimeError("unknown kind")

    fig, ax = plt.subplots(constrained_layout=True, figsize=(6.5, 4))
    ax.scatter(v_r_interp, γ_interp, label="Extrapolated")
    ax.scatter(v_r_unassist, γ_unassist, label="Unassisted")
    ax.legend()
    ax.set_xlabel("$v_{r}$")
    ax.set_ylabel("$γ$")
    fig.savefig(args.save_file)

if __name__ == '__main__':
    main()
