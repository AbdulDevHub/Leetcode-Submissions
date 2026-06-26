class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            vowelCounter = 0
            for i in range(query[0], query[1]+1):
                vowelCounter += validWord(words[i])
            result.append(vowelCounter)
        return result

def validWord(word):
    return 1 if (word[0] in 'aeiou' and word[-1] in 'aeiou') else 0