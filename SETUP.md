# Environment setup

## Local preparation

Use Python 3.12. Download or clone this repository, open a terminal in its root, and create an isolated environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux with `source .venv/bin/activate`, or on Windows PowerShell with `.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open `instructor/first_model.ipynb`. Run cells from top to bottom. Then open the Day 1 worked notebook. A notebook is a document containing text and executable code cells; all cells share the active kernel's variables.

## Before class

- Download the entire repository and install dependencies while online.
- Keep `datasets/retail_orders.csv` beside the course folders, preserving the repository structure.
- Restart the kernel and run all cells. This catches accidental dependence on variables from an earlier run.
- Save executed copies locally, including charts and outputs, as the demonstration fallback.
- Do not install or upgrade packages during a live lesson unless necessary.

## Troubleshooting

| Symptom | Action |
|---|---|
| ModuleNotFoundError | Install requirements in the same environment used by the notebook kernel. |
| Dataset not found | Open Jupyter from the repository root; keep all folders together. |
| A variable is undefined | Restart the kernel and run cells in order. |
| A chart does not appear | Re-run its cell and check for an earlier exception. |
| An output differs slightly | Check versions; compare the interpretation, not only rounded decimals. |

## Days 2–5

The core requirements now include SciPy and statsmodels. Days 2–4 and the local neural/GAN examples use this core environment. The toy GAN is implemented with NumPy/SciPy and does not require PyTorch, a GPU or an online API.

For the standalone Spark lab, install Java 17 first and confirm `java -version`. Ensure the Java executable is on PATH; if setting JAVA_HOME, point it to the installed JDK directory. Then, in the active Python environment:

```bash
python -m pip install -r requirements-spark.txt
```

PySpark is a large download: install and test before class. Open day-05-big-data/spark_worked.ipynb and run all cells. It starts a local session with two threads and stops it at the end. Notebook data are generated locally, so no internet is needed after dependencies are installed. If Spark fails, use the saved outputs and OFFLINE_ACTIVITY.md; do not spend the lesson installing it.

## Automated rehearsal (optional)

```bash
python -m pip install -r requirements-validation.txt
python -m ipykernel install --user --name course-validation --display-name "Course validation"
python scripts/check_notebook_kernels.py
```

This runs the four solution notebooks and the separate Spark notebook in fresh kernels. `scripts/validate_days.py` executes worked cells and refreshes text/SVG outputs. `scripts/build_days_02_05.py` rebuilds the worked/student source notebooks only; it does not regenerate teaching guides or exercise solutions. Do not use the builder casually after making notebook edits.

The environment was checked on Linux with Python 3.12 and Java 17. Windows/macOS installation and the classroom laptops still need rehearsal.

