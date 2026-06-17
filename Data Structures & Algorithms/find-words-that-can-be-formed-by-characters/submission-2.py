class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Count character frequencies in 'chars'
        char_counts = [0] * 26
        for c in chars: char_counts[ord(c) - ord('a')] += 1
        
        # Step 2: Check each word against the counts
        total_length = 0
        for word in words:
            word_counts = [0] * 26
            is_valid = True
            for c in word:
                idx = ord(c) - ord('a')
                word_counts[idx] += 1
                # Early exit if we exceed the available characters
                if word_counts[idx] > char_counts[idx]:
                    is_valid = False
                    break
            
            if is_valid: total_length += len(word)
        return total_length