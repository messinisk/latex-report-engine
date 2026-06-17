
# 📘 **latex-report-engine**  
*A modular LaTeX reporting engine for data analysis workflows.*  
**Μια modular μηχανή δημιουργίας LaTeX αναφορών για data analysis workflows.**

---

# 🇬🇧 **English Version**

## 📌 Overview  
`latex-report-engine` is a modular Python engine that generates clean, reproducible LaTeX reports using templates for sections, figures, and tables.  
It is designed for data analysts, data scientists, and automation pipelines that require PDF reporting without LaTeX boilerplate.

---

## 🖥️ System Requirements

To compile reports into PDF, your system must have:

### **Python**
- Python **3.9+**

### **LaTeX Distribution (required for PDF output)**
You must have a full LaTeX distribution installed:

- **TeX Live** (Linux, macOS, Windows)  
- **MiKTeX** (Windows)  
- **MacTeX** (macOS)

The engine uses **XeLaTeX or LuaLaTeX**, so they must be available in your PATH:

```bash
xelatex --version
lualatex --version
```

### **Required LaTeX Packages**
Your LaTeX installation must include:

- `graphicx`
- `booktabs`
- `float`
- `geometry`

(Most distributions include them by default.)

---

## 📦 Installation (pip)

Install directly from GitHub:

```bash
pip install git+https://github.com/messinisk/latex-report-engine.git
```

This installs:

- the `report_engine` Python module  
- LaTeX builders (sections, figures, tables)  
- the PDF exporter  
- all templates (`base.tex`, `section.tex`, `figure.tex`, `table.tex`)  

---

## 🚀 Example Usage

```python
from report_engine.latex_builder import LatexReport
from report_engine.exporters import Exporter

# 1. Create a new report
report = LatexReport(title="Sales Analysis Report")

# 2. Add a section
report.add_section(
    title="Executive Summary",
    content="This report provides an overview of sales performance."
)

# 3. Add a figure
report.add_figure(
    path="plots/sales_trend.png",
    caption="Sales Trend Over Time",
    width="0.9\\textwidth"
)

# 4. Add a LaTeX table
table_latex = r"""
\begin{tabular}{lrr}
\toprule
Product & Units Sold & Revenue \\
\midrule
A & 120 & 5400 \\
B & 80 & 3200 \\
C & 150 & 7500 \\
\bottomrule
\end{tabular}
"""

report.add_table(table_content=table_latex)

# 5. Export to PDF
Exporter.to_pdf(report, output_path="output/report.pdf")
```

---

## 🧩 Template Structure

The engine uses Jinja‑like LaTeX templates:

- `base.tex` — document wrapper  
- `section.tex` — dynamic sections  
- `figure.tex` — figures with captions  
- `table.tex` — LaTeX tables  

---

## 🎯 Features

- Clean, modular architecture  
- Zero LaTeX boilerplate inside notebooks  
- Reproducible PDF reports  
- Plug‑and‑play templates  
- Ideal for automated pipelines  

---

# 🇬🇷 **Ελληνική Έκδοση**

## 📌 Επισκόπηση  
Το `latex-report-engine` είναι μια modular Python μηχανή που δημιουργεί καθαρές, αναπαραγώγιμες LaTeX αναφορές χρησιμοποιώντας templates για sections, εικόνες και πίνακες.  
Σχεδιάστηκε για data analysts, data scientists και pipelines που χρειάζονται PDF reports χωρίς LaTeX spaghetti code.

---

## 🖥️ Απαιτήσεις Συστήματος

Για να γίνει compile σε PDF, το σύστημα πρέπει να έχει:

### **Python**
- Python **3.9+**

### **LaTeX Distribution (απαραίτητο για PDF)**
Πρέπει να υπάρχει εγκατεστημένο ένα πλήρες LaTeX distribution:

- **TeX Live**  
- **MiKTeX**  
- **MacTeX**

Το engine χρησιμοποιεί **XeLaTeX ή LuaLaTeX**, άρα πρέπει να υπάρχουν στο PATH:

```bash
xelatex --version
lualatex --version
```

### **Απαραίτητα LaTeX Packages**
Το σύστημα πρέπει να διαθέτει:

- `graphicx`
- `booktabs`
- `float`
- `geometry`

(Συνήθως είναι ήδη εγκατεστημένα.)

---

## 📦 Εγκατάσταση (pip)

Εγκατάσταση απευθείας από GitHub:

```bash
pip install git+https://github.com/messinisk/latex-report-engine.git
```

Αυτό εγκαθιστά:

- το Python module `report_engine`  
- τους builders για sections, figures, tables  
- τον PDF exporter  
- όλα τα templates (`base.tex`, `section.tex`, `figure.tex`, `table.tex`)  

---

## 🚀 Παράδειγμα Χρήσης

```python
from report_engine.latex_builder import LatexReport
from report_engine.exporters import Exporter

report = LatexReport(title="Sales Analysis Report")

report.add_section(
    title="Executive Summary",
    content="This report provides an overview of sales performance."
)

report.add_figure(
    path="plots/sales_trend.png",
    caption="Sales Trend Over Time",
    width="0.9\\textwidth"
)

table_latex = r"""
\begin{tabular}{lrr}
\toprule
Product & Units Sold & Revenue \\
\midrule
A & 120 & 5400 \\
B & 80 & 3200 \\
C & 150 & 7500 \\
\bottomrule
\end{tabular}
"""

report.add_table(table_content=table_latex)

Exporter.to_pdf(report, output_path="output/report.pdf")
```

---

## 🧩 Δομή Templates

Το πακέτο χρησιμοποιεί Jinja‑like templates:

- `base.tex` — βασικό document wrapper  
- `section.tex` — δυναμικά sections  
- `figure.tex` — εικόνες με captions  
- `table.tex` — LaTeX πίνακες  

---

## 🎯 Τι προσφέρει

- Modular αρχιτεκτονική  
- Καθαρός κώδικας χωρίς LaTeX μέσα σε notebooks  
- Αναπαραγώγιμες αναφορές  
- Plug‑and‑play templates  
- Ιδανικό για αυτοματοποιημένα pipelines  
