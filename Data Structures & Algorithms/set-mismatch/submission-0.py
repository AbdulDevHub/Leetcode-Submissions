class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        detectiveList = [0]*(len(nums)+1)
        for num in nums: detectiveList[num] += 1

        missingNum = 0
        repeatedNum = 0
        for i, num in enumerate(detectiveList):
            if num == 0: missingNum = i
            if num == 2: repeatedNum = i
        
        return[repeatedNum, missingNum]