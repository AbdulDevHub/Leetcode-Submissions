class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.isqrt(8 * n + 1) - 1) // 2)