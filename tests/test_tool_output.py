from agent_lab.tool_output import compact_test_output

def test_successful_output():
    """Successful tests should have a success status."""
    result = compact_test_output(
        stdout="5 passed",
        stderr="",
        returncode=0,
    )

    assert result["success"] is True
    assert result["exit_code"] == 0


def test_failed_output():
    """Failed tests should preserve error information."""
    result = compact_test_output(
        stdout="test_example FAILED",
        stderr="AssertionError",
        returncode=1,
    )

    assert result["success"] is False
    assert result["exit_code"] == 1
    assert "test_example FAILED" in result["important_lines"]


def test_large_output():
    """Long outputs should be compressed."""
    long_output = "\n".join(
        f"Log line {i}" for i in range(1000)
    )

    result = compact_test_output(
        stdout=long_output,
        stderr="",
        returncode=0,
    )

    assert len(result["tail"]) <= 30
    assert result["total_lines"] >= 1000