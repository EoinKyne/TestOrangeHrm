import subprocess
import sys
from pathlib import Path


def run_tests(
        tests_path: str = "orangehrm_tests",
        headed: bool = False,
        browser: str | None = None,
        extra_args: list[str] | None = None,
) -> int:
    cmd = [sys.executable, "-m", "pytest", tests_path]

    if headed:
        cmd.append("--headed")

    if browser:
        cmd.append(f"--browser={browser}")

    if extra_args:
        cmd.append(extra_args)

    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd)
    return result.returncode
