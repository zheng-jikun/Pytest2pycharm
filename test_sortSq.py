from sortSq import custom_sort
import pytest

def test_custom_sort():
    """
    This test verifies if `custom_sort` function works correctly
    only for one specific input list.
    """
    # Preparation of test data
    unsorted_list = [3, 1, 2]
    expected_sorted_list = [1, 2, 3]

    # Run the tested code
    function_return_value = custom_sort(unsorted_list)

    # Verify if the value returned from the function matches
    # the expected value.
    assert function_return_value == expected_sorted_list
