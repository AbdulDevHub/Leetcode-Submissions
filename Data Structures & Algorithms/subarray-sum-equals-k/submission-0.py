class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, curSum = 0, 0
        prefixSums = { 0 : 1 } # Base case: handles when curSum exactly equals k
        for num in nums:
            curSum += num      # Update running total
            diff = curSum - k  # The needed value from past to make sum of k
            result += prefixSums.get(diff, 0) # If 'diff' seen before, valid subarray exists
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return result