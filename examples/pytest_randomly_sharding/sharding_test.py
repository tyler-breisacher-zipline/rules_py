import pytest


@pytest.mark.parametrize("case_index", range(31))
def test_case(case_index: int) -> None:
    """Fails if case_index is 0, passes in all other cases."""
    assert case_index != 0
