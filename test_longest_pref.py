from longet_common_prefix_14 import *


def test_solution_1():
    test_case_1 = ["flower", "flow", "flight"]
    test_case_2 = ["dog","racecar","car"]
    result = "fl"
    result2 = ""
    test_result = solution_1(test_case_1)
    assert result == test_result
    test_result = solution_1(test_case_2)
    assert result2 == test_result
