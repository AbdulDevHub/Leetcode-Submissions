class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()  # Stores elements in non-increasing order
        minDeque = deque()  # Stores elements in non-decreasing order
        left, maxLength = 0, 0
        for right, val in enumerate(nums):
            # Maintain maxDeque (remove smaller elements from back)
            while maxDeque and maxDeque[-1] < val: maxDeque.pop()
            maxDeque.append(val)
            
            # Maintain minDeque (remove larger elements from back)
            while minDeque and minDeque[-1] > val: minDeque.pop()
            minDeque.append(val)
            
            # Shrink window if max - min exceeds limit
            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[left]: maxDeque.popleft()
                if minDeque[0] == nums[left]: minDeque.popleft()
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        return maxLength

# ==============================================================================
# HOW THIS SOLUTION WORKS:
# ==============================================================================
#
# 1. SLIDING WINDOW PATTERN:
#    - Uses two pointers (`left` and `right`) to represent a dynamic subarray window:
#      `nums[left...right]`.
#    - The `right` pointer iterates through the array, expanding the window one
#      element at a time.
#    - The `left` pointer contracts the window whenever the condition is broken
#      (i.e., when max_val - min_val > limit).
#
# 2. MONOTONIC DEQUES (DOUBLE-ENDED QUEUES):
#    To keep track of the maximum and minimum elements in the current window in O(1)
#    time, two monotonic deques are maintained:
#    
#    - `maxDeque`:
#      Maintains candidate maximums in decreasing order.
#      `maxDeque[0]` ALWAYS holds the current maximum value in the window.
#      Before adding `val`, elements smaller than `val` are popped from the back
#      because they can never be the maximum again while `val` is present.
#
#    - `minDeque`:
#      Maintains candidate minimums in increasing order.
#      `minDeque[0]` ALWAYS holds the current minimum value in the window.
#      Before adding `val`, elements larger than `val` are popped from the back
#      because they can never be the minimum again while `val` is present.
#
# 3. WINDOW CONTRACTION:
#    - When `maxDeque[0] - minDeque[0] > limit`, the window is invalid.
#    - We shrink the window from the left by incrementing `left`.
#    - If `nums[left]` matches `maxDeque[0]` or `minDeque[0]`, that value is leaving
#      our window, so we pop it from the front of the corresponding deque.
#
# 4. TRACKING THE RESULT:
#    - After ensuring the window is valid, `maxLength` is updated with the current
#      window length: `right - left + 1`.
#
# ==============================================================================
# COMPLEXITY ANALYSIS:
# ==============================================================================
# - Time Complexity:  O(N)
#   Each element is pushed into and popped from `maxDeque` and `minDeque` at most
#   once, leading to amortized O(1) ops per iteration across the N elements.
#
# - Space Complexity: O(N)
#   In the worst case (e.g., strictly increasing or decreasing arrays), the deques
#   may store up to N elements.
# ==============================================================================
