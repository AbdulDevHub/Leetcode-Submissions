class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ""

        # Frequency map for target characters
        target_counts = Counter(t)
        missing = len(t)  # Total remaining characters needed
        l = start = end = 0
        min_len = float("inf")
        for r, char in enumerate(s):
            # If char was needed, decrement our missing count
            if target_counts[char] > 0: missing -= 1
            # Decrement char count in map (can go negative for extra chars)
            target_counts[char] -= 1

            # When window is valid, contract from left
            while missing == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start, end = l, r + 1

                # Put left character back into the requirement balance
                target_counts[s[l]] += 1
                if target_counts[s[l]] > 0:
                    missing += 1
                l += 1
        return s[start:end] if min_len != float("inf") else ""