"""Rebuild every benchmark case into benchmarks/cases/.

Usage: python3 benchmarks/builder/build_all.py [case-script-stem ...]
Stdlib only. Each script in cases/ parses its answer sheet and writes cases.
"""

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

only = set(sys.argv[1:])
for script in sorted((HERE / "cases").glob("*.py")):
    if only and script.stem not in only:
        continue
    runpy.run_path(str(script), run_name="__main__")
    print(f"built {script.stem}")
