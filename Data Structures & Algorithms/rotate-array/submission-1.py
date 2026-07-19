class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

#         # 1. Reverse everything: [7, 6, 5, 4, 3, 2, 1]
#         reverse(0, n - 1)
#         # 2. Reverse first k:    [5, 6, 7, 4, 3, 2, 1]
#         reverse(0, k - 1)
#         # 3. Reverse the rest:   [5, 6, 7, 1, 2, 3, 4]
#         reverse(k, n - 1)