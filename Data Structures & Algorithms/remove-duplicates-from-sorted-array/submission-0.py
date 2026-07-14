class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:       
        writePtr = 1 
        for readPtr in range(1, len(nums)):
            if nums[readPtr] != nums[readPtr - 1]:
                nums[writePtr] = nums[readPtr]
                writePtr += 1
        return writePtr