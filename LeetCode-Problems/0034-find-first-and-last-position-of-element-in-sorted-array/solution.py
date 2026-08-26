class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def binarySearch(target):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target: right = mid
                else: left = mid + 1
            return left

        start = binarySearch(target)
        if start == n or nums[start] != target: return [-1, -1]
        return [start, binarySearch(target + 1) - 1]
