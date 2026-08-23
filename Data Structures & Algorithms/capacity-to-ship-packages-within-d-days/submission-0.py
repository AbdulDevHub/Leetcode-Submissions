class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)  # [1]
        res = right

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days: return False  # [2]
                    currCap = cap
                currCap -= w
            return True

        while left <= right:
            cap = (left + right) // 2
            if canShip(cap):
                res = min(res, cap)
                right = cap - 1  # [3]
            else:
                left = cap + 1
        return res

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# Approach: Binary search on the answer space (capacity), using a greedy 
# simulation to test if a candidate capacity fits all packages in D days.
#
# [1] Search Space Bounds:
#     The absolute minimum valid capacity must be max(weights) so the largest
#     single package can fit on a ship. The upper bound sum(weights) represents
#     shipping everything in 1 day.
#
# [2] Early Exit Guard:
#     Short-circuits the simulation the moment required ships exceed the day
#     limit, avoiding unnecessary iterations for invalid capacities.
#
# [3] Monotonic Shrink:
#     Since any capacity >= a valid capacity will also work, finding a valid
#     cap allows us to record it and search left for a smaller valid minimum.