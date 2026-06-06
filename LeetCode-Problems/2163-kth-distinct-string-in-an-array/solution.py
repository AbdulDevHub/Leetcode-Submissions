class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for string in arr: count[string] = count.get(string, 0) + 1
        
        for string in arr:
            if count[string] == 1:
                k -= 1
                if k == 0: return string
        return ""
