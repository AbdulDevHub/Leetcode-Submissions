class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result, left, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            result += (right - left + 1)
        return result