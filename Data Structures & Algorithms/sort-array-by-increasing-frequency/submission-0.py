class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numDict = Counter(nums)
        # Keys are sorted descending by negating them (-item[0])
        orderedDict = dict(sorted(numDict.items(), key=lambda item: (item[1], -item[0])))
        return [key for key, value in orderedDict.items() for _ in range(value)]