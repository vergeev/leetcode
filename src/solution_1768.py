#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for c1, c2 in zip_longest(word1, word2):
            if c1:
                merged.append(c1)
            if c2:
                merged.append(c2)
        return ''.join(merged)
# @lc code=end

