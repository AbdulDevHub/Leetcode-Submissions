class Solution:

  def splitArray(self, nums: List[int], k: int) -> int:

    # Helper function: Counts how many subarrays are needed
    # if no single subarray sum can exceed 'max_allowed_sum'.
    def count_subarrays(max_allowed_sum: int) -> int:
      subarrays = 1
      current_sum = 0

      for num in nums:
        # If adding the current number exceeds our target sum,
        # we MUST start a new subarray.
        if current_sum + num > max_allowed_sum:
          subarrays += 1
          current_sum = num  # Reset current sum with the new element
        else: current_sum += num
      return subarrays

    low = max(nums)
    high = sum(nums)
    # BINARY SEARCH ON ANSWER:
    while low < high:
      mid = (low + high) // 2
      if count_subarrays(mid) <= k: high = mid
      else: low = mid + 1
    return low
