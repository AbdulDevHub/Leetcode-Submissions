class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = sorted(nums1 + nums2)
        n = len(m)
        return (m[n // 2] + m[(n - 1) // 2]) / 2