class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            if (r - l + 1) * nums[r] > total + k:
                total -= nums[l]
                l += 1
        return len(nums) - l