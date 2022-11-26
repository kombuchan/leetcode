class Solution:
    def countBits(self, n: int) -> List[int]:
                                                 #         Time         #Space
        if n == 0:                               #         O(1)            
            return [0]                           #         O(1)           O(1)       
        if n == 1:                               #         O(1)
            return [0, 1]                        #         O(1)           O(1)
        
        memo = []                                #                        O(1) - if output space not included. 
        memo.append(0)                           #         O(1)           O(1)
        memo.append(1)                           #         O(1)           O(1)
        
        offset = 2                               #         O(1)           O(1)
        
        for i in range(2, n + 1):                #         O(N)           
            if i == 2 * offset:                  #         O(1) 
                offset = i                       #         O(1)           O(1)

            memo.append(1 + memo[i - offset])    #         O(1)           O(1)
                
        return memo                              #         O(1)            
    
                                                 # ------------------------------------------
                                                 #         O(N)         O(1)