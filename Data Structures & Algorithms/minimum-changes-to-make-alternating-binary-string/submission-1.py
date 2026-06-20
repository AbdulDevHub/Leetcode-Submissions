class Solution:
    def minOperations(self, s: str) -> int:
        # Count how many characters mismatch the "0101..." pattern
        count_start_0 = sum(int(char) != i % 2 for i, char in enumerate(s))
        # The cost for the "1010..." pattern is just the remaining characters
        return min(count_start_0, len(s) - count_start_0)