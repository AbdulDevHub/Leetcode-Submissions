class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}  # [1]
        left = 0
        result = 0
        for right in range(len(s)):
            char = s[right]
            if char in mp:
                left = max(mp[char] + 1, left)  # [2]
            
            mp[char] = right  # [3]
            result = max(result, right - left + 1)  # [4]

        return result

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# [1] Character Index Hash Map:
#     Stores the most recent index seen for each character ({char: index}) 
#     to allow O(1) duplicate lookups.
#
# [2] Window Boundary Adjustment:
#     Moves 'left' to one position past the duplicate's last seen index. 
#     'max()' prevents 'left' from moving backward if the duplicate occurred 
#     outside the current active window (e.g., handling cases like "abba").
#
# [3] Index Tracking:
#     Records or updates the latest index location of the current character.
#
# [4] Max Window Update:
#     Calculates the length of the current valid substring (right - left + 1) 
#     and updates 'result' if it exceeds the maximum found so far.
