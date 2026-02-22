import numpy as np
import xarray as xr

# Exact example from the problem statement
da = xr.DataArray(np.arange(24), dims=["time"])
da = da.assign_coords(day=365 * da)
ds = da.to_dataset(name="T")

print("Before coarsen.construct:")
print(ds)
print()

result = ds.coarsen(time=12).construct(time=("year", "month"))

print("After coarsen.construct:")
print(result)
print()

# Verify the fix
print("✓ Verification:")
print(f"  - 'day' is still a coordinate: {'day' in result.coords}")
print(f"  - 'day' is not a data variable: {'day' not in result.data_vars}")
print(f"  - 'T' is still a data variable: {'T' in result.data_vars}")
