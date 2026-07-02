class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            outputArr[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            outputArr[i] *= suffix
            suffix *= nums[i]
        return outputArr
