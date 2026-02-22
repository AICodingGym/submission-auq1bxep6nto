import xarray as xr
from xarray.testing import assert_identical

def test_where_attrs() -> None:
    cond = xr.DataArray([True, False], coords={"a": [0, 1]}, attrs={"attr": "cond_da"})
    cond["a"].attrs = {"attr": "cond_coord"}
    x = xr.DataArray([1, 1], coords={"a": [0, 1]}, attrs={"attr": "x_da"})
    x["a"].attrs = {"attr": "x_coord"}
    y = xr.DataArray([0, 0], coords={"a": [0, 1]}, attrs={"attr": "y_da"})
    y["a"].attrs = {"attr": "y_coord"}

    # 3 DataArrays, takes attrs from x
    print("Test 1: 3 DataArrays, takes attrs from x")
    actual = xr.where(cond, x, y, keep_attrs=True)
    expected = xr.DataArray([1, 0], coords={"a": [0, 1]}, attrs={"attr": "x_da"})
    expected["a"].attrs = {"attr": "x_coord"}
    try:
        assert_identical(expected, actual)
        print("✅ PASSED")
    except AssertionError as e:
        print(f"❌ FAILED: {e}")

    # x as a scalar, takes no attrs
    print("\nTest 2: x as a scalar, takes no attrs")
    actual = xr.where(cond, 0, y, keep_attrs=True)
    expected = xr.DataArray([0, 0], coords={"a": [0, 1]})
    try:
        assert_identical(expected, actual)
        print("✅ PASSED")
    except AssertionError as e:
        print(f"❌ FAILED: {e}")

    # y as a scalar, takes attrs from x
    print("\nTest 3: y as a scalar, takes attrs from x")
    actual = xr.where(cond, x, 0, keep_attrs=True)
    expected = xr.DataArray([1, 0], coords={"a": [0, 1]}, attrs={"attr": "x_da"})
    expected["a"].attrs = {"attr": "x_coord"}
    try:
        assert_identical(expected, actual)
        print("✅ PASSED")
    except AssertionError as e:
        print(f"❌ FAILED: {e}")

    # x and y as a scalar, takes no attrs
    print("\nTest 4: x and y as scalars, takes no attrs")
    actual = xr.where(cond, 1, 0, keep_attrs=True)
    expected = xr.DataArray([1, 0], coords={"a": [0, 1]})
    try:
        assert_identical(expected, actual)
        print("✅ PASSED")
    except AssertionError as e:
        print(f"❌ FAILED: {e}")

    # cond as a scalar, takes attrs from x
    print("\nTest 5: cond as a scalar, takes attrs from x")
    actual = xr.where(True, x, y, keep_attrs=True)
    expected = xr.DataArray([1, 1], coords={"a": [0, 1]}, attrs={"attr": "x_da"})
    expected["a"].attrs = {"attr": "x_coord"}
    try:
        assert_identical(expected, actual)
        print("✅ PASSED")
    except AssertionError as e:
        print(f"❌ FAILED: {e}")

if __name__ == "__main__":
    test_where_attrs()
    print("\n✅ All tests completed successfully!")
