class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If lightest and heaviest person can share boat
            if people[left] + people[right] <= limit:
                left += 1  # Lightest person gets on board
            
            # Heaviest person always gets boat (shared or alone)
            right -= 1
            boats += 1
            
        return boats