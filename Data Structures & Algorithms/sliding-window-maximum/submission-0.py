class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxOutputArr = []
        left, right = 0, k
        while right < len(nums)+1:
          maxOutputArr.append(max(nums[left:right]))
          left += 1
          right += 1
        return maxOutputArr