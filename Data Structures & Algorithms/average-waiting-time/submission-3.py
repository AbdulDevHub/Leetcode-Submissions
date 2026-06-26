class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time = 0
        current_time = 0
        for arrival, time_needed in customers:
            current_time = max(current_time, arrival) + time_needed
            total_wait_time += current_time - arrival
        return total_wait_time / len(customers)