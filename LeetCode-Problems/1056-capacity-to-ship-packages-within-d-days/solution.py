class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)  # [1]
        res = right

        def canShip(cap):  # [2]
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days: return False
                    currCap = cap
                currCap -= w
            return True

        while left <= right:  # [3]
            cap = (left + right) // 2
            if canShip(cap):
                res = min(res, cap)
                right = cap - 1
            else:
                left = cap + 1
        return res

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# Approach: Binary search on the answer space (capacity), using a greedy 
# simulation helper to test if a candidate capacity fits all packages in D days.
#
# [1] Search Space Bounds:
#     The minimum capacity must be max(weights) so the single heaviest package 
#     fits. The maximum capacity is sum(weights), which ships everything in 1 day.
#
# [2] Feasibility Check (Greedy Pack):
#     Simulates packing packages sequentially into ships. We greedily fill each 
#     ship to its max capacity before starting a new one. If total ships needed 
#     exceeds `days`, this capacity is too small.
#
# [3] Binary Search Range Decision:
#     Capacity has a monotonic property: if capacity `cap` works, any larger 
#     capacity also works. Thus, when `canShip` is True, record `cap` as a potential 
#     minimum and search left (`right = cap - 1`). If False, increase capacity (`left = cap + 1`).
