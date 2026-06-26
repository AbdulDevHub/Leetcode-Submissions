class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        pref = [0] * (n + 1)
        for i in range(n):
            is_valid = 1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0
            pref[i + 1] = pref[i] + is_valid
            
        result = []
        for l, r in queries: result.append(pref[r + 1] - pref[l])
        return result