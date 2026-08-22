class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                ans = mid       # Valid speed, try to find a smaller one
                right = mid - 1
            else: left = mid + 1  # Too slow, need higher speed
                
        return ans
