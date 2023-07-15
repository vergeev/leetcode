"""https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ = nums1[:m]
        p1, p2, i = 0, 0, 0
        while p1 < m or p2 < n:
            if p1 >= m and p2 < n:
                nums1[i] = nums2[p2]
                p2 += 1
            elif p2 >= n and p1 < m:
                nums1[i] = nums1_[p1]
                p1 += 1
            elif p1 < m and p2 < n and nums1_[p1] <= nums2[p2]:
                nums1[i] = nums1_[p1]
                p1 += 1
            elif p1 < m and p2 < n and nums1_[p1] > nums2[p2]:
                nums1[i] = nums2[p2]
                p2 += 1
            i += 1
