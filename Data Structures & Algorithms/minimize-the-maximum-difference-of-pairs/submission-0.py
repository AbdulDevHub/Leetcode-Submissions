class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_form_p_pairs(max_diff: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip both used elements
                else:
                    i += 1  # Try the next adjacent pair
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if can_form_p_pairs(mid):
                right = mid  # Try finding a smaller maximum difference
            else:
                left = mid + 1  # Difference too small, increase target
                
        return left