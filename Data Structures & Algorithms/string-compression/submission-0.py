class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character itself
            chars[write] = char
            write += 1
            
            # If the character appeared more than once, write its count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        # The new length of the compressed array is simply the write index
        return write