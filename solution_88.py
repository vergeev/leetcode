"""https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1;
        p1 = m - 1;
        p2 = n - 1;
        while p1 > -1 or p2 > -1:
            if p1 == -1 and p2 > -1:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p2 == -1 and p1 > -1:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif p1 > -1 and p2 > -1 and nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            elif p1 > -1 and p2 > -1 and nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
