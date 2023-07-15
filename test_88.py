import pytest
from solution_88 import Solution


@pytest.mark.parametrize(
    ("num1", "m", "num2", "n", "expected_result"),
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [0], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
)
def test_solution(num1, m, num2, n, expected_result):
    result = num1
    Solution().merge(
        nums1=result,
        m=m,
        nums2=num2,
        n=n,
    )
    assert result == expected_result
