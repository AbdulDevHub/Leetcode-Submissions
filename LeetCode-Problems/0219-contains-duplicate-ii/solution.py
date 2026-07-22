class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window: return True
            window.add(nums[R])
        return False

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         window = set()
#         for i, num in enumerate(nums):
#             if num in window:
#                 return True
#             window.add(num)
            
#             # Maintain sliding window size of k
#             if len(window) > k:
#                 window.remove(nums[i - k])
#         return False
