class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        cookie_ptr = 0
        satisfied_children = 0
        num_cookies = len(s)
        
        for child_greed in g:
            # Find the first cookie that can satisfy the current child
            while cookie_ptr < num_cookies and s[cookie_ptr] < child_greed:
                cookie_ptr += 1
            
            # If we ran out of cookies, we are done
            if cookie_ptr >= num_cookies: break
                
            # We matched a cookie to a child!
            satisfied_children += 1
            cookie_ptr += 1  # Move to the next cookie for the next child
            
        return satisfied_children