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

The current requirements support Day 1 and the first-model notebook. Spark, Bayesian sampling and neural-network environments will be specified with their labs; they are not installed by this starter package.
