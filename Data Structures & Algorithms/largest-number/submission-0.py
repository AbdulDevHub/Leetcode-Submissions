class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numsStr = [str(num) for num in nums]
        
        # Multiplying by 10 ensures strings are long enough to compare properly 
        # (e.g., "3" vs "30" becomes "333..." vs "303030...")
        numsStr.sort(key=lambda x: x * 10, reverse=True)
        
        # Edge Case: largest number "0" (e.g., [0, 0])
        if numsStr[0] == "0": return "0"
        return "".join(numsStr)