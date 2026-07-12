class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # If mismatch occurs, try skipping either left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True
