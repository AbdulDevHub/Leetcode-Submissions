class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Check if any adjacent elements have the same parity
        for a, b in zip(nums, nums[1:]):
            if (a % 2) == (b % 2):
                return False
        return True
