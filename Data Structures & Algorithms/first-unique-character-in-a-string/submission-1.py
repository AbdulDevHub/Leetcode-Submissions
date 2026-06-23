class Solution:
    def firstUniqChar(self, s: str) -> int:
        # We only need to check the unique characters present in s
        ans = [s.index(c) for c in set(s) if s.find(c) == s.rfind(c)]
        return min(ans) if ans else -1