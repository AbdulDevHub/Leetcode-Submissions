class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map to store { remainder : first_seen_index }
        remainder_map = {0: -1}
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            remainder = curSum % k
            if remainder in remainder_map:
                # Check if subarray length >= 2
                if i - remainder_map[remainder] >= 2: return True
            else: remainder_map[remainder] = i
        return False