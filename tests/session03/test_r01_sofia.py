from challenge_tools import (
    verify_python_version
)

def test_python_version_is_3_10_or_newer():
    """R-01: Se utiliza Python 3.10 o superior."""
    assert verify_python_version() is True