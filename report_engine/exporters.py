# exporters.py
from pathlib import Path
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT))


class Exporter:

    def __init__(self, output_dir="exports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    # -----------------------------
    # DataFrame → LaTeX
    # -----------------------------
    def table(self, df: pd.DataFrame, filename: str):
        latex_str = df.to_latex(index=False)
        path = self.output_dir / f"{filename}.tex"
        path.write_text(latex_str, encoding="utf-8")
        return path

    # -----------------------------
    # Plot → PNG
    # -----------------------------
    def plot(self, plt_obj, filename: str):
        path = self.output_dir / f"{filename}.png"
        plt_obj.savefig(path, dpi=300, bbox_inches="tight")
        plt_obj.close()
        return path

    # -----------------------------
    # Raw LaTeX → file
    # -----------------------------
    def latex(self, content: str, filename: str):
        path = self.output_dir / f"{filename}.tex"
        path.write_text(content, encoding="utf-8")
        return path
