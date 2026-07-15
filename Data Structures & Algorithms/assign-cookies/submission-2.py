class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gPointer = 0
        sPointer = 0
        
        while gPointer < len(g) and sPointer < len(s):
            if s[sPointer] >= g[gPointer]:
                gPointer += 1
            sPointer += 1
        return gPointer