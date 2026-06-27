import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(start, end):
            # Base Case
            if start >= end: return

            # Anti Hackers
            randIndex = random.randint(start, end)
            nums[randIndex], nums[end] = nums[end], nums[randIndex]

            # Main Loic
            pivot = nums[end]
            boundary = start
            for j in range(start, end):
                if nums[j] < pivot:
                    nums[j], nums[boundary] = nums[boundary], nums[j]
                    boundary += 1
            nums[boundary], nums[end] = nums[end], nums[boundary]

            # 3 Quick Sorts
            quicksort(start, boundary - 1)
            quicksort(boundary + 1, end)
        quicksort(0, len(nums) - 1)