class RandomizedSet:

    def __init__(self):
        # Maps the value to its current index in the elementList
        self.valueToIndexMap = {}
        # Stores the actual values for O(1) random selection
        self.elementList = []

    def insert(self, val: int) -> bool:
        if val in self.valueToIndexMap:
            return False
        
        # Map the value to its future index in the array
        self.valueToIndexMap[val] = len(self.elementList)
        self.elementList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueToIndexMap:
            return False
        
        # Get the index of the element to delete and the last element
        targetIndex = self.valueToIndexMap[val]
        lastElement = self.elementList[-1]
        
        # Swap: Move the last element into the spot of the element we are removing
        self.elementList[targetIndex] = lastElement
        self.valueToIndexMap[lastElement] = targetIndex
        
        # Clean up: Remove the last element from the list and delete from map
        self.elementList.pop()
        del self.valueToIndexMap[val]
        
        return True

    def getRandom(self) -> int: 
        # Since elementList contains exactly our current elements,
        # random.choice guarantees a completely uniform distribution in O(1).
        return random.choice(self.elementList)
