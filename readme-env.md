# Project environment with uv

Guide to set up the Python environment for this project using [uv](https://docs.astral.sh/uv/). uv also downloads and manages the Python version, so you do not need to install Python separately.

## 1. Install uv

On Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check the installation:

```bash
uv --version
```

## 2. Create the environment and install dependencies

Dependencies are declared in [pyproject.toml](pyproject.toml) and the Python version (3.12) in `.python-version`. From the project root:

```bash
uv sync
```

This downloads Python 3.12 (if needed), creates `.venv` and installs everything, respecting the exact versions pinned in `uv.lock`. A single environment covers all notebooks (`gen_dataset`, `stats`, `tsne`, `figures`, `test_model_error` and `train_symbolic_regression`).

## 3. Activate the environment

```powershell
.venv\Scripts\activate          # Windows (PowerShell/cmd)
```

```bash
source .venv/bin/activate       # Linux/macOS
```

You can also run commands without activating it, e.g. `uv run jupyter notebook`.

## 4. Manage packages

```bash
uv add <package>      # add (updates pyproject.toml and uv.lock)
uv remove <package>   # remove
uv lock --upgrade     # upgrade versions
uv sync               # sync the environment with the lock file
```

## 5. PySR (symbolic regression)

`pysr` requires Julia. On the first run (`import pysr` or creating a `PySRRegressor`) it automatically downloads and installs Julia and the required packages. This may take a few minutes and requires an internet connection. Later runs use the cache.

## 6. Use the environment in VS Code / Jupyter

Register the kernel for the notebooks:

```bash
python -m ipykernel install --user --name rimes-env --display-name "Python (rimes-env)"
```

In VS Code, open a notebook, click **Select Kernel** and choose `.venv` (or `Python (rimes-env)`).

To open Jupyter in the browser:

```bash
jupyter notebook
```

## 7. Deactivate or recreate the environment

```bash
deactivate
```

To recreate it from scratch, delete the `.venv` folder and run `uv sync` again.

> The `.venv` folder is not part of the repository. To ignore it in git, add `.venv/` to `.gitignore`.
