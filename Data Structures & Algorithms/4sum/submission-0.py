from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        n = len(nums)

        def kSum(k, start, target):
            # Base Case: 2-Sum
            if k == 2:
                left, right = start, n - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum < target: left += 1
                    elif curr_sum > target: right -= 1
                    else:
                        res.append(quad + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return

            # Early Pruning & Boundary Checks
            for i in range(start, n - k + 1):
                # Skip duplicate elements
                if i > start and nums[i] == nums[i - 1]: continue
                # 1. Too Large: Even the smallest elements sum to more than target
                if nums[i] * k > target: break
                # 2. Too Small: Even with the largest elements, we can't reach target
                if nums[i] + (k - 1) * nums[-1] < target: continue

                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res