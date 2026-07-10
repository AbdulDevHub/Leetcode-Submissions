class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justifiedArr = []
        justifiedLine = ""
        
        for word in words:
            # Check if word fits. If justifiedLine is empty, we don't need an extra space yet.
            current_len = len(justifiedLine) + len(word) + (1 if justifiedLine else 0)
            
            if current_len <= maxWidth: 
                if justifiedLine:
                    justifiedLine += " " + word
                else:
                    justifiedLine = word
            else: 
                # Line is full, justify it normally
                justifiedArr.append(Solution.spaceEvenly(justifiedLine, maxWidth, isLast=False))
                justifiedLine = word
                
        # Handle the very last line remaining after the loop (must be left-justified)
        if justifiedLine:
            justifiedArr.append(Solution.spaceEvenly(justifiedLine, maxWidth, isLast=True))
            
        return justifiedArr

    @staticmethod
    def spaceEvenly(line: str, maxWidth: int, isLast: bool) -> str:
        words = line.split(" ")
        num_words = len(words)
        
        # Scenario 1: Only 1 word in the line OR it's the last line of the paragraph
        if num_words == 1 or isLast:
            res = " ".join(words)
            return res + " " * (maxWidth - len(res))
            
        # Scenario 2: Normal full justification
        # Total characters belonging to actual words
        total_word_chars = sum(len(w) for w in words)
        total_spaces = maxWidth - total_word_chars
        
        num_gaps = num_words - 1
        wordSeperatorFreq = total_spaces // num_gaps
        wordSeperatorRemainder = total_spaces % num_gaps
        
        newLine = ""
        for i in range(num_gaps):
            newLine += words[i]
            # Add base spaces + 1 extra space if we are still within the remainder count
            actual_spaces = wordSeperatorFreq + (1 if i < wordSeperatorRemainder else 0)
            newLine += " " * actual_spaces
            
        newLine += words[-1] # Append the final word
        return newLine