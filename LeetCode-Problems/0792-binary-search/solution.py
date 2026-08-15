# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return self.binarySearch(0, len(nums) - 1, nums, target)

#     def binarySearch(self, l: int, r: int, nums: List[int], target: int) -> int:
#         if l > r: return -1
#         mid = (l + r) // 2
#         if nums[mid] == target: return mid
#         elif nums[mid] > target: 
#             return self.binarySearch(l, mid - 1, nums, target)
#         else:
#             return self.binarySearch(mid + 1, r, nums, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return -1
