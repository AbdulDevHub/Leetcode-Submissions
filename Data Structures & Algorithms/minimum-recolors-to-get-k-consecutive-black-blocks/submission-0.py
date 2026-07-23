class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count 'W's in the initial window of size k
        whiteCount = blocks[:k].count('W')
        minConversionOps = whiteCount

        # Slide the window across the string
        for i in range(k, len(blocks)):
            whiteCount += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            minConversionOps = min(minConversionOps, whiteCount)
        return minConversionOps