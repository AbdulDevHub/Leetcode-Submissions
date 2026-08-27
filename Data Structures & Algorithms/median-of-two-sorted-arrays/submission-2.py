class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = sorted(nums1 + nums2)
        n = len(m)
        # Averages middle 2 nums if even len; 
        # averages middle num with itself if odd
        return (m[n // 2] + m[(n - 1) // 2]) / 2