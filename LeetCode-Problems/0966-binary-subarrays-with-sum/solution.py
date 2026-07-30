class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0: return 0
            left = 0
            current_sum = 0
            subarrays = 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                subarrays += (right - left + 1)
            return subarrays
        return atMost(goal) - atMost(goal - 1)


"""
================================================================================
FOOTER REFERENCE & NOTES
================================================================================

Problem: LeetCode 930 - Binary Subarrays With Sum
Strategy: Sliding Window / At-Most Pattern

1. CORE INTUITION:
   - Directly sliding a window for exact target sums in arrays with zeros is tricky 
     because zero-values allow flexible window boundaries.
   - We reframe the problem using inclusion-exclusion:
     
     Exact(goal) = AtMost(goal) - AtMost(goal - 1)

2. AT-MOST SLIDING WINDOW LOGIC:
   - Expands `right` pointer to include new elements into `current_sum`.
   - Shrinks `left` pointer whenever `current_sum > k`.
   - When the window [left...right] is valid (sum <= k), the total number of valid 
     subarrays ENDING at index `right` is `(right - left + 1)`.

3. EDGE CASES:
   - k < 0: Returns 0 since binary array elements are non-negative, so sums < 0 
     are impossible.
   - goal = 0: `atMost(0) - atMost(-1)` correctly evaluates `atMost(0) - 0`.

4. COMPLEXITY:
   - Time Complexity: O(N) -> Two passes of O(N) sliding window operations.
   - Space Complexity: O(1) -> Only uses constant extra pointers and variables.
================================================================================
"""
