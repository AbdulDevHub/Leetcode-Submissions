class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            sub = str(i) * 3
            if sub in num: return sub
        return ""