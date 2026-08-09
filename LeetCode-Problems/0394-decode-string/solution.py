class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != "[":              # [1]
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():  # [2]
                    k = stack.pop() + k
                stack.append(int(k) * substr)          # [3]

        return "".join(stack)

# ==============================================================================
# FOOTER NOTES
# ==============================================================================
# Approach: Single stack holding both raw characters and fully-decoded
# substrings. On hitting ']', pop back to the matching '[' to recover the
# innermost group, then pop any digits before it to get the repeat count,
# and push the expanded result back onto the stack as one unit.
#
# [1] Pop until matching bracket:
#     Characters pushed since the last unmatched '[' are exactly the
#     contents of the innermost group (digits and brackets from outer
#     groups can't have leaked in, since inner groups always close first).
#     Popping in order and prepending rebuilds the substring left-to-right.
#
# [2] Collect multi-digit counts:
#     Repeat counts can be more than one digit (e.g. "12[a]"), so digits
#     are popped one at a time and prepended until a non-digit (or empty
#     stack) is hit, reassembling the full number.
#
# [3] Push expanded group as one stack entry:
#     Pushing the repeated string (not the individual chars) lets an outer
#     group later scoop it up whole when its own ']' is processed — this is
#     what lets nested groups like "2[a3[b]]" resolve correctly.
