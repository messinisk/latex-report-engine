# latex_builder.py
from pathlib import Path
# Get the absolute path of the current file
file_path = Path(__file__).resolve()
print("File Path:", file_path)
# Get the directory containing the current file
directory_path = file_path.parent
print("Directory Path:", directory_path)
from pathlib import Path

class LatexReport:

    def __init__(self, filename, output_dir="reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.filename = filename
        self.content = []

        self._add_header()

    # -----------------------------
    # INTERNAL: LaTeX header/footer
    # -----------------------------
    def _add_header(self):
        self.content.append(r"""
\documentclass{article}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{float}

\begin{document}
""")

    def _add_footer(self):
        self.content.append(r"\end{document}")

    # -----------------------------
    # PUBLIC API
    # -----------------------------
    def add_section(self, title):
        self.content.append(fr"\section*{{{title}}}")

    def add_text(self, text):
        self.content.append(text)

    def add_figure(self, image_path, width="0.9\\textwidth"):
        self.content.append(fr"""
\begin{{figure}}[H]
\centering
\includegraphics[width={width}]{{{image_path}}}
\end{{figure}}
""")

    def add_table(self, latex_table_str):
        self.content.append(latex_table_str)

    def add_file(self, latex_file_path):
        text = Path(latex_file_path).read_text(encoding="utf-8")
        self.content.append(text)

    def save(self):
        self._add_footer()
        final = "\n".join(self.content)
        path = self.output_dir / f"{self.filename}.tex"
        path.write_text(final, encoding="utf-8")
        return path
