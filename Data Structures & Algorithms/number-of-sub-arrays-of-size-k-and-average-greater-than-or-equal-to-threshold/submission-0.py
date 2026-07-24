class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        validSubarrays = 0
        # Loop up to point where full window of size k fits
        for i in range(len(arr) - k + 1):
            if sum(arr[i:i+k]) / k >= threshold: validSubarrays += 1
        return validSubarrays