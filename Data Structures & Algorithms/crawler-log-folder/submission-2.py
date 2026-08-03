class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for command in logs:
            if command == "../":
                if depth > 0: depth -= 1
            elif command != "./": depth += 1
        return depth