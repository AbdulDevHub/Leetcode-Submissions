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

1. THE CORE IDEA (Exact K via Difference of At Most):
   Finding subarrays with *exactly* K distinct integers directly using a single 
   sliding window is difficult because moving the left pointer can either maintain 
   or destroy valid states unpredictably.
   
   We use a standard mathematical identity for ranges:
       Exact(K) = AtMost(K) - AtMost(K - 1)
   
   - `atMost(k)` calculates the total count of contiguous subarrays containing 
     at most K distinct integers.
   - `atMost(k - 1)` calculates the count of contiguous subarrays containing 
     at most K - 1 distinct integers.
   - Subtracting the two gives the total count of subarrays containing EXACTLY K
     distinct integers.

2. HOW THE SLIDING WINDOW WORKS (`atMost(goal)`):
   - Expand: We iterate the `right` pointer to include `nums[right]` in our hash map (`freq`).
   - Shrink: If `len(freq)` (number of distinct elements) exceeds `goal`, we increment 
     the `left` pointer, decrementing element counts until `len(freq) <= goal`.
   - Count: For every valid window `[left, right]`, the number of contiguous subarrays 
     ending at index `right` with at most `goal` distinct elements is equal to the 
     window length: `(right - left + 1)`.

3. COMPLEXITY ANALYSIS:
   - Time Complexity: O(N)
     Each element is visited at most twice by the `right` and `left` pointers. 
     Hash map operations (lookup, insert, delete) take O(1) average time.
     
   - Space Complexity: O(N)
     In the worst case, the `freq` map stores up to N unique integers.
================================================================================
"""
