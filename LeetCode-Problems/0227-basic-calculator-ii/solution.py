class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operator = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # Process operator or end of string (ignoring whitespace)
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack.append(stack.pop() * current_num)
                elif operator == '/':
                    # int() ensures division truncates toward zero in Python
                    stack.append(int(stack.pop() / current_num))
                
                operator = char
                current_num = 0
                
        return sum(stack)

# ==============================================================================
# ALGORITHM FOOTER & IMPLEMENTATION NOTES
# ==============================================================================
# Strategy: Stack-Based Operator Precedence Parsing
# 
# How it Works:
# 1. Deferred Evaluation (+ / -): Push numbers (or their negative value for subtraction) 
#    onto the stack to defer addition/subtraction until the entire string is read.
# 2. Immediate Evaluation (* / /): Pop the top element, perform the operation with 
#    the current number, and push the result back onto the stack to respect operator precedence.
# 3. Final Aggregation: Sum all values remaining in the stack.
#
# Key Python Edge Cases Handled:
# - Multi-digit numbers: Reconstructed via `current_num = current_num * 10 + int(char)`.
# - Trailing whitespaces: Ignored during parsing; evaluation triggers on non-spaces or end of string.
# - Division truncation: Python's floor division (`//`) rounds toward negative infinity 
#   (e.g., -3 // 2 = -2). Using `int(a / b)` truncates toward zero (e.g., int(-3 / 2) = -1),
#   matching standard LeetCode specifications.
#
# Complexity:
# - Time Complexity: O(n) — Single pass over the string of length n.
# - Space Complexity: O(n) — In the worst case, the stack stores O(n) numbers.
# ==============================================================================
