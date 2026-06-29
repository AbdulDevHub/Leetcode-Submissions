class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        finalString = ""
        for char in order:
            if char in s: 
                finalString += char*count[char]
                del count[char]
        for key, value in count.items():
            for _ in range(value): finalString += key
        return finalString    