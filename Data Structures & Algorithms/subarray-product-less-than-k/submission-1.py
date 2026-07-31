class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        res = 0
        logs = [0] * (n + 1)
        logK = log(k)
        for i in range(n):
            logs[i + 1] = logs[i] + log(nums[i])

        for i in range(n):
            l, r = i + 1, n + 1
            while l < r:
                mid = (l + r) >> 1
                if logs[mid] < logs[i] + logK - 1e-9:
                    l = mid + 1
                else:
                    r = mid
            res += l - (i + 1)

        return res