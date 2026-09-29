# pytest-randomly with Bazel test sharding

The pytest shard plugin assigns tests by their position in the collected list.
`pytest-randomly` can put that list in a different order in each Bazel shard
process. A test may then run twice, while another test is skipped entirely.

This example has 31 parametrized cases and eight Bazel shards. Its collection
hook checks that each shard selected the test IDs assigned by Finn's stable
hash and round-robin algorithm. On a version of `rules_py` with the
position-based algorithm, the target fails and reports missing and unexpected
test IDs. With the fix, each case is assigned to exactly one shard, and the
shard sizes differ by at most one.

Run from this directory:

```sh
bazel test //:sharded_test --test_output=errors
```
