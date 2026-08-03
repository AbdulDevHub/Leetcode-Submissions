class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for command in logs:
            if len(stack) > 0 and command == "../": stack.pop()
            elif len(stack) == 0 and command == "../": continue
            elif command == "./": continue
            else: stack.append(command)
        return len(stack)