from bisect import bisect_left, bisect_right
import math

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n2 = len(nums2)
        def count_less_or_equal(target: int) -> int:
            total = 0
            for x in nums1:
                if x > 0:
                    # x * y <= target  =>  y <= target // x
                    # bisect_right finds how many elements in nums2 are <= (target // x)
                    total += bisect_right(nums2, target // x)
                elif x < 0:
                    # x * y <= target  =>  y >= target / x
                    # bisect_left finds index of first element >= math.ceil(target / x)
                    bound = math.ceil(target / x)
                    total += n2 - bisect_left(nums2, bound)
                else: # x == 0
                    if target >= 0: total += n2
            return total

        # Lower bound: max negative product (-10^5 * 10^5)
        # Upper bound: max positive product (10^5 * 10^5)
        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if count_less_or_equal(mid) >= k: high = mid
            else: low = mid + 1
        return low
