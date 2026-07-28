class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n1])
        if s1_count == window_count: return True

        for i in range(n1, n2):
            # Slide window right: add incoming character
            window_count[s2[i]] += 1
            
            # Slide window right: remove outgoing character
            left_char = s2[i - n1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Direct O(1) comparison of at most 26 character frequencies
            if s1_count == window_count: return True

        return False
