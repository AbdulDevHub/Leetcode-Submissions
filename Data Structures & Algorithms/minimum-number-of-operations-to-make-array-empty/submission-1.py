class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        numOfOperations = 0     
        for key in numCount:
            if numCount[key] == 1: return -1

            threeTakeaway = numCount[key] // 3
            # EDGE CASE: If taking this many 3s leaves exactly 1 remaining,
            # we must back off by one group of 3 to leave 4 elements (which splits into two 2s).
            if numCount[key] % 3 == 1: threeTakeaway -= 1
            numCount[key] -= 3 * threeTakeaway
            
            twoTakeaway = numCount[key] // 2
            numCount[key] -= 2 * twoTakeaway
            
            if numCount[key] != 0: return -1                
            numOfOperations += threeTakeaway + twoTakeaway
            
        return numOfOperations