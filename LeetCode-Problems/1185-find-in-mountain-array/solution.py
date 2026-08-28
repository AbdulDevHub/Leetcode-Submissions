# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # 1. Find the peak of the mountain array
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else: right = mid
        peak = left

        # 2. Search in the strictly increasing left side [0, peak]
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target: return mid
            elif val < target: left = mid + 1
            else: right = mid - 1

        # 3. Search in the strictly decreasing right side [peak + 1, n - 1]
        left, right = peak + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target: return mid
            elif val > target: left = mid + 1 # Order reversed for decreasing side
            else: right = mid - 1
        return -1
