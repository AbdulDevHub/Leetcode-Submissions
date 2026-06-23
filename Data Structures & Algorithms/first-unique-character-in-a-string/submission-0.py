class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueDict = {}
        for i, char in enumerate(s):
            if char not in uniqueDict: uniqueDict[char] = i
            else: uniqueDict[char] = "N/A"
        for key in uniqueDict:
            if uniqueDict[key] != "N/A": return uniqueDict[key]
        return -1