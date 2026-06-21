class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        totalLetterMap = {}
        for word in words:
            for letter in word:
                totalLetterMap[letter] = totalLetterMap.get(letter, 0) + 1
        for value in totalLetterMap.values():
            if value % len(words) != 0: return False
        return True
