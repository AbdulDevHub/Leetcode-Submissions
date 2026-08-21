class Solution:

  def singleNonDuplicate(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) // 2
      # Ensure mid is even to easily compare with mid + 1
      if mid % 2 == 1: mid -= 1
      # If pair matches, single element is on the right
      if nums[mid] == nums[mid + 1]: left = mid + 2
      # Otherwise, single element is at or to the left of mid
      else: right = mid
    return nums[left]