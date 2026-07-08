class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        numOfOperations = 0
        for count in numCount.values():
            if count == 1: return -1
            # (count + 2) // 3 is the mathematical equivalent of math.ceil(count / 3)
            numOfOperations += (count + 2) // 3
        return numOfOperations
