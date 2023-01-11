from sortSq import custom_sort
import pytest

def test_custom_sort():

    # test data
    unsorted_list = [3, 1, 2]
    expected_sorted_list = [1, 2, 3]

    function_return_value = custom_sort(unsorted_list)

    assert function_return_value == expected_sorted_list
