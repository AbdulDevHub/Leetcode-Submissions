class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing, is_decreasing = True, True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]: is_increasing = False
            if nums[i] < nums[i+1]: is_decreasing = False
            if not is_increasing and not is_decreasing: return False
        return True
