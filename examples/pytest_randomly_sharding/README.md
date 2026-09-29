# pytest-randomly with Bazel test sharding

The pytest shard plugin assigns tests by their position in the collected list.
`pytest-randomly` can put that list in a different order in each Bazel shard
process. A test may then run twice, or get skipped entirely.

```sh
bazel test //:sharded_test --test_output=errors
```
