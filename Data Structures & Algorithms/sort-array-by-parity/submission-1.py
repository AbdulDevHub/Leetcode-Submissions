class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] % 2 == 0:
                nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
                write_idx += 1
        return nums