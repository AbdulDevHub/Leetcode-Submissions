class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []
        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]
        for char, val in count.items(): res.append(char * val)
        return "".join(res)
