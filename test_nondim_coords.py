import numpy as np
import xarray as xr

# Test the issue with non-dimensional coordinates
def test_coarsen_construct_preserves_nondim_coords():
    """Test that coarsen.construct preserves non-dimensional coordinates."""
    da = xr.DataArray(np.arange(24), dims=["time"])
    da = da.assign_coords(day=365 * da)
    ds = da.to_dataset(name="T")
    
    print("Before coarsen.construct:")
    print("Dataset:", ds)
    print("Coordinates:", dict(ds.coords))
    print("Data variables:", list(ds.data_vars))
    print("Is 'day' a coordinate?", 'day' in ds.coords)
    print()
    
    result = ds.coarsen(time=12).construct(time=("year", "month"))
    
    print("After coarsen.construct:")
    print("Dataset:", result)
    print("Coordinates:", dict(result.coords))
    print("Data variables:", list(result.data_vars))
    print("Is 'day' a coordinate?", 'day' in result.coords)
    print()
    
    # Check that 'day' is still a coordinate
    assert 'day' in result.coords, "Non-dimensional coordinate 'day' was demoted to a variable!"
    assert 'day' not in result.data_vars, "'day' should not be a data variable!"
    
    # Check that T is still a data variable
    assert 'T' in result.data_vars, "'T' should be a data variable!"
    assert 'T' not in result.coords, "'T' should not be a coordinate!"
    
    print("✓ Test passed: Non-dimensional coordinates are preserved")

if __name__ == "__main__":
    test_coarsen_construct_preserves_nondim_coords()
