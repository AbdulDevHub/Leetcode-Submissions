class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        max_len = -1
        for i, char in enumerate(s):
            if char in first_seen:
                current_len = i - first_seen[char] - 1
                max_len = max(max_len, current_len)
            else: first_seen[char] = i
        return max_len
