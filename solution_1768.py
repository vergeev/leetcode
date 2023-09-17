#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        try:
            for c1, c2 in zip(word1, word2, strict=True):
                merged.append(c1)
                merged.append(c2)
        except ValueError:
            if len(word1) > len(word2):
                merged.append(word1[len(word2):])
            else:
                # len(word1) < len(word2) 
                merged.append(word2[len(word1):])
        return ''.join(merged)
# @lc code=end

