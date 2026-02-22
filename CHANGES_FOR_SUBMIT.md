Fix: preserve coordinate attrs in xr.where(..., keep_attrs=True)

This repository contains a small fix to avoid applying a callable
`combine_attrs` to coordinate merging, which could overwrite coordinate
attributes when `keep_attrs=True` is passed to `xr.where`.

Added regression test: `xarray/tests/test_where_keep_attrs.py`.

This file was added to force a new commit for resubmission.
