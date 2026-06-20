from pathlib import Path
import os
import subprocess
import sys

root = Path("C:/Users/mithi/OneDrive/Desktop") / "\u00A0" / "codealpha_task" / "task"
print(f"Project root: {root}")
if not root.exists():
    raise FileNotFoundError(f"Expected project root does not exist: {root}")
os.chdir(root)
venv_dir = root / ".venv"
if not venv_dir.exists():
    import venv
    venv.create(venv_dir, with_pip=True)
python_exec = venv_dir / "Scripts" / "python.exe"
if not python_exec.exists():
    raise FileNotFoundError(f"Virtualenv python not found: {python_exec}")
subprocess.check_call([str(python_exec), "-m", "pip", "install", "-r", str(root / "requirements.txt")])
subprocess.check_call([str(python_exec), "-m", "pytest", "-q", str(root / "tests")])
print("Validation complete")
