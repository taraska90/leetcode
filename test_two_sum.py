from two_sum import *


def test_solution():
    nums = [3, 2, 3]
    target = 6
    result = solution(nums, target)
    assert result is 6


def test_solution_2():
    nums = [3, 2, 3]
    target = 6
    result = solution_2(nums, target)
    assert result is [0, 2]
