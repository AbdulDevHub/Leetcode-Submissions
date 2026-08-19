class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        remainingCoins = n
        for i in range(1, n + 1):
            if remainingCoins >= i:
                count += 1
                remainingCoins -= i
            else: break
        return count
