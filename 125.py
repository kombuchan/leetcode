class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_str = ""
        for char in s:
            if char.isalnum(): # o(1)
                stripped_str += char.lower() #o(1), o(n)
                
        mid = len(stripped_str)//2
   
        #odd length
        if len(stripped_str)%2:
            i=1
            while(i<=mid):
                if stripped_str[mid-i] != stripped_str[mid+i]: return False
                i+=1
            return True

        #even length
        else:                   
            if len(stripped_str) == 2 and stripped_str[0] != stripped_str[1]: return False
            i=1
            while(i<mid):
                if stripped_str[mid-i] != stripped_str[mid+i-1]: return False
                i+=1
            return True