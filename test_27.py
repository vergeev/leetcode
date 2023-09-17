import pytest
from solution_27 import Solution

@pytest.mark.parametrize(
    ("nums", "val", "expected_nums"),
    [
        ([1, 2, 3, 4, 5, 6, 1, 7, 1], 1, [2, 3, 4, 5, 6, 7]),
        ([], 1, []),
        ([1], 1, []),
    ]
)
def test_solution(nums, val, expected_nums):
    k = Solution().removeElement(nums, val)

    assert k == len(expected_nums);
    assert list(sorted(nums[:k])) == expected_nums
