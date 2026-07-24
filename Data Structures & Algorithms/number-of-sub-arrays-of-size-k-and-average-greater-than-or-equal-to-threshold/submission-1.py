class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        current_sum = sum(arr[:k])
        validSubarrays = 1 if current_sum >= target_sum else 0
        
        # Slide the window across the array
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]  # Add new right, remove old left
            if current_sum >= target_sum:
                validSubarrays += 1
                
        return validSubarrays