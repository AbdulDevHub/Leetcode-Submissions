class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

"""
===============================================================================
LEETCODE 853: CAR FLEET — MONOTONIC STACK SOLUTION
===============================================================================

Core Concept:
  1. Calculate each car's time-to-target: Time = (target - position) / speed.
  2. Process cars in sorted order of their starting position from right to left
     (closest to target first).
  3. A car behind catching up to a slower car ahead (time_behind <= time_ahead)
     forms a single fleet driven by the slower car's time.

Algorithm Steps:
  - Pair positions with speeds and sort in descending order of position.
  - Iterate through the pairs, calculate time to target, and push to stack.
  - If top of stack (behind car) <= second top (ahead car), pop the top element
    because the behind car merges into the ahead car's fleet.
  - Return the stack length (each remaining value represents one unique fleet).

Complexity Analysis:
  - Time Complexity:  O(N log N) — Dominated by sorting positions. Stack loops in O(N).
  - Space Complexity: O(N)       — Space required for zipped pairs and stack storage.
===============================================================================
"""