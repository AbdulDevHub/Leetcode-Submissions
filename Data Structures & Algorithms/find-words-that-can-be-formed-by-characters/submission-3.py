class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Count frequency of characters available
        char_counts = Counter(chars)
        total_length = 0
        
        # Step 2: Check each word
        for word in words:
            word_counts = Counter(word)
            # If word_counts is a subset of char_counts, it's valid
            # The '-' operator subtracts counts, keeping only positive results
            if not (word_counts - char_counts):
                total_length += len(word)
                
        return total_length