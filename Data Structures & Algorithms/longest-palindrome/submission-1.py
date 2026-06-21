class Solution:
    def longestPalindrome(self, s: str) -> int:
        totalLetterMap = {}
        palindromeLength = 0
        has_odd_frequency = False

        for letter in s: totalLetterMap[letter] = totalLetterMap.get(letter, 0) + 1
        for value in totalLetterMap.values():
            palindromeLength += (value // 2) * 2
            if value % 2 == 1: has_odd_frequency = True
        if has_odd_frequency: palindromeLength += 1 # place 1 odd letter in middle
            
        return palindromeLength