class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        flag = 0
        n = len(words)

        for w in words:
            for c in w:
                i = ord(c) - ord('a')
                if freq[i] != 0:
                    freq[i] += 1
                    if freq[i] % n == 0:
                        flag += 1
                else:
                    freq[i] += 1
                    if freq[i] % n != 0:
                        flag -= 1
                freq[i] %= n

        return flag == 0