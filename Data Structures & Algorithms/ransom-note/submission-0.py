class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Count character frequencies in 'magazine'
        magazineCharCount = [0] * 26
        for char in magazine: magazineCharCount[ord(char) - ord('a')] += 1
        
        # Step 2: Check ransomNote against magazineCharCount
        ransomNoteCount = [0] * 26
        for char in ransomNote:
            idx = ord(char) - ord('a')
            ransomNoteCount[idx] += 1
            if ransomNoteCount[idx] > magazineCharCount[idx]: return False
        return True