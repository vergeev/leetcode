import pytest
from src.solution_1071 import Solution


@pytest.mark.parametrize(
    ("str1", "str2", "expected_result"),
    [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("AABAABAAB", "AABAAB", "AAB"),
        ("AABAABAABAAB", "AABAAB", "AABAAB"),
        ("ABABABABABABABAB", "ABABAB", "AB"),
        ("LEET", "CODE", ""),
        ("CEET", "CODE", ""),
        ("LEE", "LEEQQQ", ""),
        ("LEET", "LEET", "LEET"),
        ("LEETLEET", "LEET", "LEET"),
        ("LEELEE", "LEE", "LEE"),
        ("LEELEE", "EELEEL", ""),
        ("LEEEE", "LEEEEE", ""),
        ("ABCBAC", "ABC", ""),
        
    ],
)
def test_solution(str1, str2, expected_result):
    assert Solution().gcdOfStrings(
        str1,
        str2,
    ) == expected_result
