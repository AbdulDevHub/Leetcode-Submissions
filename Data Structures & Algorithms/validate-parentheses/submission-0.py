class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesStack = []
        for parenthes in s:
            if len(parenthesesStack) == 0: parenthesesStack.append(parenthes)
            elif parenthes in "{[(" and parenthesesStack[-1] in "{[(":
                parenthesesStack.append(parenthes)
            elif parenthes == "]" and parenthesesStack[-1] == "[":
                parenthesesStack.pop()
            elif parenthes == "}" and parenthesesStack[-1] == "{":
                parenthesesStack.pop()
            elif parenthes == ")" and parenthesesStack[-1] == "(":
                parenthesesStack.pop()
            else: return False
        return len(parenthesesStack) == 0