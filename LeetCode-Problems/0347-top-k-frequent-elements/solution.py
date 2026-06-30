# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numCount = Counter(nums)
#         sortedKeys = sorted(numCount.keys(), key=lambda x: numCount[x], reverse=True)
#         return sortedKeys[:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        return [item[0] for item in numCount.most_common(k)]
