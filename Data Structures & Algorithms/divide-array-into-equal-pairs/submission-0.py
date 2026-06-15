class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        return all(val % 2 == 0 for val in freqMap.values())