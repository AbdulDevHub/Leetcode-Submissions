class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores indices
        result = []
        for right in range(len(nums)):
            # 1. Remove indices outside the current window
            if dq and dq[0] < right - k + 1: dq.popleft()
            # 2. Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[right]: dq.pop()
            # 3. Add current element's index
            dq.append(right)
            # 4. Record max once we have a full window of size k
            if right >= k - 1: result.append(nums[dq[0]])
        return result