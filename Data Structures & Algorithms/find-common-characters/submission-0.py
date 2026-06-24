class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize a map with the maximum possible counts from the first word
        min_counts = {}
        for char in words[0]:
            min_counts[char] = min_counts.get(char, 0) + 1
            
        # Compare with the rest of the words
        for word in words[1:]:
            current_counts = {}
            for char in word:
                current_counts[char] = current_counts.get(char, 0) + 1
            
            # Update min_counts to hold the minimum intersection
            for char in list(min_counts.keys()):
                if char in current_counts:
                    min_counts[char] = min(min_counts[char], current_counts[char])
                else:
                    del min_counts[char] # Not common to all words
                    
        # Build the final result
        res = []
        for char, count in min_counts.items():
            res.extend([char] * count)
        return res