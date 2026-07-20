class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 1000000007
        res = 0
        l, r = 0, len(nums) - 1
        
        # Precompute powers of 2: power[k] = (2^k) % MOD
        power = [1] * len(nums)
        for i in range(1, len(nums)):
            power[i] = (power[i - 1] * 2) % MOD

        while l <= r:
            if nums[l] + nums[r] <= target:
                # Add all subsequences where nums[l] is the minimum
                res = (res + power[r - l]) % MOD
                l += 1  # Move left pointer to try the next minimum
            else: r -= 1  # Sum is too big, shrink max from the right

        return res