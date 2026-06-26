class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        startTime = 0 
        customerWaitTimes = []
        for customer in customers:
            startCooking = max(startTime, customer[0])
            finishCooking = startCooking + customer[1]
            waitTime = finishCooking - customer[0]
            customerWaitTimes.append(waitTime)
            startTime = finishCooking
        return sum(customerWaitTimes) / len(customers)