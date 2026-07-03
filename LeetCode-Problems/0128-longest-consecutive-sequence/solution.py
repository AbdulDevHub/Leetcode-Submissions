class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                conSequence = 0
                while (num + conSequence) in numSet:
                    conSequence += 1
                longest = max (conSequence, longest)
        return longest
