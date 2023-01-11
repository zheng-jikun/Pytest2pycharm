import pytest


#偶数为通过  fail*1  pass*2
@pytest.mark.parametrize("arg1", [2, 4, 7])
def test_is_even(arg1):
    assert arg1 % 2 == 0

#arg1 arg2分别对应每一组数据，数据和为偶数
@pytest.mark.parametrize("arg1, arg2", [(1, 2), (3, 5)])
def test_is_sum_even(arg1, arg2):
    assert (arg1 + arg2) % 2 == 0


#没有写清排列组合的顺序所以遍历全部组合，一共4个，其中不通过的在结果中标出
@pytest.mark.parametrize("arg1", [1, 5])
@pytest.mark.parametrize("arg2", [3, 8])
def test_is_sum_even_every_combination(arg1, arg2):
    assert (arg1 + arg2) % 2 == 0