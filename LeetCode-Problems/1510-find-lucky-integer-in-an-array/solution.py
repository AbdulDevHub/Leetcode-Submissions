class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = {}
        for num in arr: freqMap[num] = freqMap.get(num, 0) + 1

        largestLuckyNum = -1
        for key, val in freqMap.items():
            if key == val and key > largestLuckyNum:
                largestLuckyNum = key
                
        return largestLuckyNum
