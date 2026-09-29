"""Enough cases to give each of eight shards several distinct test IDs."""

import pytest


@pytest.mark.parametrize("case_index", range(31))
def test_case(case_index: int) -> None:
    assert case_index in range(31)
