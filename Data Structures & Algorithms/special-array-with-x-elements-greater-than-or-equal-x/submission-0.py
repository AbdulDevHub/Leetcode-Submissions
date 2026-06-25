class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            equalOrGreaterCounter = 0
            for num in nums: 
                if num >= i: equalOrGreaterCounter += 1
            if equalOrGreaterCounter == i: return equalOrGreaterCounter
        return -1