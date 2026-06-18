class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goodIntegers = []
        numProgress = ""
        for n in num:
            if numProgress == "" or n == numProgress[0]: numProgress += n
            else: numProgress = n
            if len(numProgress) == 3: 
                goodIntegers.append(numProgress)
                numProgress = ""
        return max(goodIntegers, key=int) if goodIntegers else ""

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         goodIntegers = []
#         numProgress = ""
        
#         for n in num:
#             # If it's the same character, extend the streak
#             if numProgress == "" or n == numProgress[-1]: 
#                 numProgress += n
#             else: 
#                 # If the character changes, reset the streak to the *new* character
#                 numProgress = n
                
#             # If we hit a length of 3, it's a good integer
#             if len(numProgress) == 3: 
#                 goodIntegers.append(numProgress)
#                 # Keep the last 2 characters in case it's a longer streak like "7777"
#                 numProgress = numProgress[1:] 
                
#         return max(goodIntegers) if goodIntegers else ""