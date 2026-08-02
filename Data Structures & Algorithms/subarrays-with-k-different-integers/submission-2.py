class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(goal: int) -> int:
            if goal < 0: return 0
            freq = defaultdict(int)
            left, count = 0, 0
            for right, num in enumerate(nums):
                freq[num] += 1
                
                # Shrink window if distinct elements exceed goal
                while len(freq) > goal:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0: del freq[nums[left]]
                    left += 1
                
                # Number of valid subarrays ending at 'right' is window length
                count += (right - left + 1)
            return count
        return atMost(k) - atMost(k - 1)

"""
================================================================================
                               FOOTER EXPLANATION
================================================================================

1. WHY Exact(K) = AtMost(K) - AtMost(K - 1):
   `AtMost(K)` alone is not sufficient because it includes subarrays with 
   *fewer* than K distinct elements (i.e., 1, 2, ..., K-1 distinct elements).

   If we categorize subarrays by their count of distinct elements:

   +--------------------------+------------------+----------------------+
   | # of Distinct Elements   | AtMost(K) Count? | AtMost(K - 1) Count? |
   +--------------------------+------------------+----------------------+
   | 1 distinct element       |       YES        |         YES          |
   | 2 distinct elements      |       YES        |         YES          |
   | ...                      |       YES        |         YES          |
   | K - 1 distinct elements  |       YES        |         YES          |
   | K distinct elements      |       YES        |          NO          |
   +--------------------------+------------------+----------------------+

   Both functions overlap on all subarrays containing 1 through K - 1 distinct 
   elements. Subtracting AtMost(K - 1) cancels out all those unwanted subsets, 
   leaving ONLY the subarrays with EXACTLY K distinct elements.

2. WHY WE USE THIS TRICK (Sliding Window Monotonicity):
   A sliding window requires a strict monotonic condition:
   - For AtMost(K), the condition is clear:
       * Valid state  : len(freq) <= goal (expand right pointer)
       * Invalid state: len(freq) > goal  (shrink left pointer)

   - For Exact(K), there is no single boundary condition. Adding or removing an 
     element might maintain K distinct elements or change the state unpredictably, 
     making a standard two-pointer approach prone to missing valid windows.

3. HOW `atMost(goal)` WORKS:
   - Expand `right`: Add `nums[right]` to `freq`.
   - Shrink `left`: While `len(freq) > goal`, remove elements from the left.
   - Count: `(right - left + 1)` adds the number of valid contiguous subarrays 
     ending at index `right`.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(N) — Left and right pointers traverse the array once per call.
   - Space Complexity: O(N) — Up to N unique elements stored in the frequency map.
================================================================================
"""