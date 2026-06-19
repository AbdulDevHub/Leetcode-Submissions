class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        uniqueSorted = sorted(nums)
        return (uniqueSorted[-1] * uniqueSorted[-2]) - (uniqueSorted[0] * uniqueSorted[1])