class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Handle cases where k is larger than the array length
        # (e.g., rotating an array of size 3 by 4 spaces is the same as rotating by 1)
        k %= len(nums)
        
        # Negative indices (-k) count backward from the end of the array.
        # Example for nums = [1, 2, 3, 4, 5, 6, 7] and k = 3:
        #   nums[-3:] -> Last 3 elements: [5, 6, 7]
        #   nums[:-3] -> Everything before them: [1, 2, 3, 4]
        #   Combination: [5, 6, 7] + [1, 2, 3, 4] = [5, 6, 7, 1, 2, 3, 4]
        # The [:] overwrites the original list in-place so LeetCode registers the change.
        nums[:] = nums[-k:] + nums[:-k]