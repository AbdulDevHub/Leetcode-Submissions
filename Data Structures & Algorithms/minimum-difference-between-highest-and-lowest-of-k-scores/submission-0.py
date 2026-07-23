class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort(reverse=True)
        minDiff = float('inf')
        
        # Loop up point where full window of size k fits
        for i in range(len(nums) - k + 1):
            current_diff = nums[i] - nums[i + k - 1]
            minDiff = min(minDiff, current_diff)
        return minDiff