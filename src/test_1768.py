import pytest
from src.solution_1768 import Solution


@pytest.mark.parametrize(
    ("word1", "word2", "expected_result"),
    [
        ("123", "abcde", "1a2b3cde"),
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ],
)
def test_solution(word1, word2, expected_result):
    assert Solution().mergeAlternately(
        word1,
        word2,
    ) == expected_result
