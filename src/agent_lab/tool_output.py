import json
import subprocess
import sys


def compact_test_output(
    stdout: str,
    stderr: str,
    returncode: int,
) -> dict:
    """
    Compress test output into a structured summary.

    Preserve the execution status, important error lines,
    and the final lines of the test output.
    """

    # Combine standard output and error output.
    lines = (stdout + "\n" + stderr).splitlines()

    # Identify lines that indicate test failures or errors.
    important = [
        line for line in lines
        if "FAILED" in line or "ERROR" in line
    ]

    # Limit the size of the returned context.
    return {
        "success": returncode == 0,
        "exit_code": returncode,
        "total_lines": len(lines),
        "important_lines": [
            line[:300] for line in important[:20]
        ],
        "tail": [
            line[:300] for line in lines[-30:]
        ],
    }


def main():
    """Run local tests and display a compact report."""
    # Use the current Python interpreter.
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-vv"],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )

    # Compress the test results.
    summary = compact_test_output(
        result.stdout,
        result.stderr,
        result.returncode,
    )

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()