import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(start, end):
            if start >= end:
                return
            
            # Anti-TLE Trick: Pick a random pivot and swap it to the end
            rand_idx = random.randint(start, end)
            nums[rand_idx], nums[end] = nums[end], nums[rand_idx]
            
            # Partitioning
            pivot = nums[end]
            i = start
            for j in range(start, end):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            # Put pivot in its final place
            nums[i], nums[end] = nums[end], nums[i]
            
            # Recursively sort left and right halves
            quicksort(start, i - 1)
            quicksort(i + 1, end)

        quicksort(0, len(nums) - 1)