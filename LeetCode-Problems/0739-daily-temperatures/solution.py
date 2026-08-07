class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

# ==============================================================================
# REFERENCE & ALGORITHM SUMMARY
# ==============================================================================
# Problem: Daily Temperatures (LeetCode 739)
# Pattern: Monotonic Decreasing Stack
#
# Logic Breakdown:
# 1. Output Pre-allocation: `res` starts as all 0s; days without a warmer
#    future temperature naturally default to 0.
# 2. Monotonic Stack: `stack` stores tuples of `(temperature, index)` for days
#    waiting for a warmer day. Temperatures in the stack are kept in
#    strictly decreasing order.
# 3. Resolution Step: When current temperature `t` exceeds the stack's top
#    temperature (`stack[-1][0]`), the colder day is popped. The wait time is
#    calculated as `current_index - popped_index`.
# 4. Push Step: Current day `(t, i)` is pushed onto the stack to await future days.
#
# Complexity:
# - Time Complexity:  O(N) — Every index is pushed and popped at most once.
# - Space Complexity: O(N) — Stack holds up to N elements (worst case: descending order).
# ==============================================================================
