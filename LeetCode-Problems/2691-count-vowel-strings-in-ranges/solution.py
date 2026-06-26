class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        validWordsTotal = [0]
        for w in words:
            isValid = 1 if (w[0] in 'aeiou' and w[-1] in 'aeiou') else 0
            validWordsTotal.append(validWordsTotal[-1] + isValid)
        return [validWordsTotal[r + 1] - validWordsTotal[l] for l, r in queries]
