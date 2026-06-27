import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(start, end):
            if start >= end:
                return
            
            # Randomize pivot and swap to the start (easier for 3-way)
            rand_idx = random.randint(start, end)
            nums[rand_idx], nums[start] = nums[start], nums[rand_idx]
            
            pivot = nums[start]
            lt = start      # Elements before 'lt' are < pivot
            gt = end        # Elements after 'gt' are > pivot
            i = start + 1   # Elements between 'lt' and 'i' are == pivot
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1  # Don't increment i yet, need to check the swapped element
                else:
                    i += 1   # Equal to pivot, just move forward
            
            # Recurse only on the strictly smaller and strictly larger sections
            quicksort(start, lt - 1)
            quicksort(gt + 1, end)

        quicksort(0, len(nums) - 1)
        return nums