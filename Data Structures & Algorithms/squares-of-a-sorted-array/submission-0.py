class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        outputArr = []
        for num in nums:
            outputArr.append(num**2)
        outputArr.sort()
        return outputArr