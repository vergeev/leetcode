#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
from collections import Counter
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:        
        chars1 = Counter(str1)
        chars2 = Counter(str2)

        chars_gcd = dict(
            map(
                lambda el1, el2: (el1[0], gcd(el1[1],el2[1])),
                sorted(chars1.items()),
                sorted(chars2.items()),
            )
        )
        
        divisor_len = sum(chars_gcd.values())
        if str1[:divisor_len] != str2[:divisor_len]:
            return ""
        divisor = str1[:divisor_len]
        
        divisor_repeats1 = len(str1) // divisor_len
        divisor_repeats2 = len(str2) // divisor_len
        if divisor * divisor_repeats1 != str1:
            return ""
        if divisor * divisor_repeats2 != str2:
            return ""
        
        return divisor
# @lc code=end

