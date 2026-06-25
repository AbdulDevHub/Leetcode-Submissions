class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()
        for i in range(n): q.append(i)
        time = 0
        while q:
            time += 1
            cur = q.popleft()
            tickets[cur] -= 1
            if tickets[cur] == 0:
                if cur == k: return time
            else: q.append(cur)
        return time