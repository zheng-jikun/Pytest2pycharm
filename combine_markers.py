import pytest


@pytest.mark.parametrize("arg1", [
    1,
    pytest.param(2, marks=pytest.mark.slow),
    3,
    pytest.param(4, marks=pytest.mark.skip),
    pytest.param(5, marks=pytest.mark.xfail),
])
def test_mixing_markers(arg1):
    assert arg1 in range(5)