class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = result = 0
        for right in range(len(nums)):
            k -= (1 if nums[right] == 0 else 0)
            while k < 0:
                k += (1 if nums[left] == 0 else 0)
                left += 1
            result = max(result, right - left + 1)
        return result