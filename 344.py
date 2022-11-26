class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
                                    #          Time          Space
        l = 0                                    
        r = len(s) - 1
        
        while l < r:                #           O(N)
            temp = s[l]             #           O(1)          O(1)
            s[l] = s[r]             #           O(1)          O(1)
            s[r] = temp             #           O(1)          O(1)
            l += 1             
            r -= 1
                                    # ---------------------------------------
                                    #           O(N)          O(1)            N = length of list