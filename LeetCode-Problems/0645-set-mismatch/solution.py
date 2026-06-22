class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        repeatedNum = actual_sum - unique_sum
        missingNum = expected_sum - unique_sum
        
        return [repeatedNum, missingNum]
