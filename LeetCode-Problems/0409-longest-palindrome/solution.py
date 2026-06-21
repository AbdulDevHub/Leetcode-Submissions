class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = set()
        for char in s:
            if char in odds: odds.remove(char)
            else: odds.add(char)
        
        # If there are odd characters left, one can sit in the center
        return len(s) - len(odds) + 1 if odds else len(s)
