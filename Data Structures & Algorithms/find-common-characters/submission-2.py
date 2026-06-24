class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = Counter(words[0])
        for word in words[1:]: common_counts &= Counter(word)
        return list(common_counts.elements())