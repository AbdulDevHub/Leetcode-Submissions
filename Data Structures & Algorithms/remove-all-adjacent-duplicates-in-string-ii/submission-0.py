class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        # Each element in stack is [char, count]
        stack = []
        for char in s:
            if stack and stack[-1][0] == char: stack[-1][1] += 1
            else: stack.append([char, 1])
            # If current character count reaches k, remove it
            if stack[-1][1] == k: stack.pop()
        # Reconstruct string from remaining [char, count] pairs
        return "".join(char * count for char, count in stack)