class StockSpanner:

    def __init__(self):
        self.stack = []  # Pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        # Pop previous lower/equal prices and aggregate their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        
        # Push the current price and its combined span onto the stack
        self.stack.append((price, span))
        return span


# ==============================================================================
# TECHNICAL REFERENCE & DOCUMENTATION
# ==============================================================================
"""
Algorithm Summary: Monotonic Stack (Decreasing Order)
--------------------------------------------------------------------------------
This class computes the "stock span" (the number of consecutive days prior to and 
including today where the price was less than or equal to today's price).

Core Mechanism:
1. Every new price starts with an initial span of 1 (today itself).
2. The stack stores pairs of (price, accumulated_span) in strictly decreasing price order.
3. When a new price arrives:
   - It pops any previous prices from the stack that are LESS THAN OR EQUAL to it.
   - It absorbs (adds) the spans of those popped elements into its own span.
   - This "compression" skips redundant daily comparisons on future steps.
4. The combined (price, span) pair is pushed onto the stack.

Complexity Analysis:
--------------------------------------------------------------------------------
- Time Complexity: O(1) Amortized per call to next().
  * While the `while` loop can pop multiple elements in a single call, every element 
    is pushed onto the stack exactly ONCE and popped at most ONCE across N calls.
  * Over N calls, the total time spent in the while loop is bounded by O(N).

- Space Complexity: O(N) Worst-case.
  * In the worst case (strictly decreasing prices like [100, 80, 70, 60]), no elements
    are popped, requiring storage for up to N elements in the stack.

Trace Example:
--------------------------------------------------------------------------------
Input Sequence: [100, 80, 60, 70, 60, 75, 85]

Call       Price   Stack State (Bottom -> Top)                  Returned Span
--------------------------------------------------------------------------------
next(100)  100     [(100, 1)]                                   1
next(80)   80      [(100, 1), (80, 1)]                          1
next(60)   60      [(100, 1), (80, 1), (60, 1)]                 1
next(70)   70      [(100, 1), (80, 1), (70, 2)]                 2  (Pops 60: 1+1)
next(60)   60      [(100, 1), (80, 1), (70, 2), (60, 1)]        1
next(75)   75      [(100, 1), (80, 1), (75, 4)]                 4  (Pops 60 & 70: 1+1+2)
next(85)   85      [(100, 1), (85, 6)]                          6  (Pops 75 & 80: 1+4+1)
"""