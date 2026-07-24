class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        window = maxWindow = 0
        satisfied = 0

        for right in range(len(customers)):
            if grumpy[right]: window += customers[right]
            else: satisfied += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left]: window -= customers[left]
                left += 1
            maxWindow = max(window, maxWindow)
        return satisfied + maxWindow