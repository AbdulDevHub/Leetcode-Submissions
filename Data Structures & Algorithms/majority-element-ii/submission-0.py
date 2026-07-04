class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        numCount = Counter(nums)
        for key, value in numCount.items():
            if numCount[key] > len(nums)/3: result.append(key)
        return result