class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        currentSum = 0
        minLen = len(nums) + 1
        for right, num in enumerate(nums):
            currentSum += num
            while currentSum >= target:
                window_len = right - left + 1
                if window_len < minLen: minLen = window_len
                currentSum -= nums[left]
                left += 1
        return minLen if minLen <= len(nums) else 0
