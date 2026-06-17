class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0
        for word in words:
            validWord = True
            for wordChar in word:
                if wordChar not in allowed: validWord = False
            if validWord: total += 1
        return total