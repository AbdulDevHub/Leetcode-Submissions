class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sortedNumsSet = sorted(set(nums))
        curPositive = 1
        for num in sortedNumsSet:
            if num > 0 and num != curPositive:
                return curPositive
            elif num > 0: curPositive += 1
        return curPositive