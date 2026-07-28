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

# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         total = res = 0
#         l = 0
#         for r in range(len(nums)):
#             total += nums[r]
#             while nums[r] * (r - l + 1) > total + k:
#                 total -= nums[l]
#                 l += 1
#             res = max(res, r - l + 1)
#         return res