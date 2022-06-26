# Longest Substring Without Repeating Characters 
# OPTIMAL: Sliding window + set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longestSubstr = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longestSubstr = max(longestSubstr, r - l + 1)
        return longestSubstr
            
            
        
        
