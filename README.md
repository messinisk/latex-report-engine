# latex-report-engine
A modular LaTeX reporting engine for data analysis workflows.

## Installation & Usage Example

<code> pip install git+https://github.com/messinisk/latex-report-engine.git </code>
## System Requirements
For latex-report-engine to compile to PDF, you need:

### 1. Python
- Python 3.9+

### 2. LaTeX Distribution (required for PDF output)
A full LaTeX distribution must be installed, such as:

- TeX Live (Linux, macOS, Windows)

- MiKTeX (Windows)

- MacTeX (macOS)

The package uses XeLaTeX or LuaLaTeX, so they must be available in the PATH:
- xelatex --version
- lualatex --version

### 3.Required LaTeX Packages
The system must have the following LaTeX packages installed:
- graphicx

- booktabs

- float

- geometry

(Most distributions already have them pre-installed.)

## Example Usage

- from report_engine.latex_builder import LatexReport
- from report_engine.exporters import Exporter

### 1. Create a new report
- report = LatexReport(title="Sales Analysis Report")

### 2. Add a section
- report.add_section(
    title="Executive Summary",
    content="This report provides an overview of sales performance."
)

### 3. Add a figure
- report.add_figure(
    path="plots/sales_trend.png",
    caption="Sales Trend Over Time",
    width="0.9\\textwidth"
)

### 4. Add a LaTeX table
- table_latex = r"""
\\begin{tabular}{lrr}
\\toprule
Product & Units Sold & Revenue \\\\
\\midrule
A & 120 & 5400 \\\\
B & 80 & 3200 \\\\
C & 150 & 7500 \\\\
\\bottomrule
\\end{tabular}
"""
- report.add_table(table_content=table_latex)

### 5. Export to PDF
- Exporter.to_pdf(report, output_path="output/report.pdf")

## Example 

What this example does
Creates a new LaTeX report with a title.

Adds a section with text.

Inserts an image with a template (figure.tex).

Inserts a table with a template (table.tex).

Compiles to PDF via the Exporter.

🔧 Templates Structure (for reference)
The templates used by the engine:

 - base.tex — basic document wrapper

 - section.tex — template for sections

 - figure.tex — template for figures

 - table.tex — template for tables

 - All use Jinja‑like placeholders ({{ variable }}).


