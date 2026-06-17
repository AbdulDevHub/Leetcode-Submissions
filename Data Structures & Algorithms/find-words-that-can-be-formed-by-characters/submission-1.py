class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lenght = 0
        for word in words:
            validWord = True
            charsCompare = chars
            for wordChar in word:
                if wordChar not in charsCompare: 
                    validWord = False
                    break
                else: charsCompare = charsCompare.replace(wordChar, "", 1)
            if validWord: lenght += len(word)
        return lenght