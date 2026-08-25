class TimeMap:

    def __init__(self):
        # Store key -> list of (timestamp, value) pairs
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap.get(key, [])
        
        # Binary search for the largest timestamp <= target timestamp
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Found a valid candidate, save it
                left = mid + 1        # Keep searching right for a closer match
            else: right = mid - 1     # Mid timestamp is too large, search left
        return res
