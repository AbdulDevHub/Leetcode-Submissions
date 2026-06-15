class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_elements = set()
        for num in nums:
            if num in odd_elements: odd_elements.remove(num)
            else: odd_elements.add(num)
        return len(odd_elements) == 0
