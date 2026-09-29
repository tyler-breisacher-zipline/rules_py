"""Check shard membership after pytest-randomly and rules_py's shard plugin run."""

import hashlib
import os

import pytest


def pytest_collection_finish(session: pytest.Session) -> None:
    shard_count = int(os.environ["TEST_TOTAL_SHARDS"])
    shard_id = int(os.environ["TEST_SHARD_INDEX"])
    assert shard_count == 8
    assert session.items

    module_id = session.items[0].nodeid.split("::", maxsplit=1)[0]
    nodeids = [f"{module_id}::test_case[{index}]" for index in range(31)]
    ranked_nodeids = sorted(
        nodeids,
        key=lambda nodeid: (hashlib.sha256(nodeid.encode()).digest(), nodeid),
    )
    expected = set(ranked_nodeids[shard_id::shard_count])
    actual = {item.nodeid for item in session.items}
    assert actual == expected, (
        f"shard {shard_id}: missing {sorted(expected - actual)}, "
        f"unexpected {sorted(actual - expected)}"
    )
