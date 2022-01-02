# Longest Substring Without Repeating Characters 

# NAIVE 
# 
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longestSubstr = 0
#         for i in range(len(s)):
#             seen = set()
#             substr = ''
#             j = i
#             while j < len(s) and s[j] not in seen:
#                 seen.add(s[j])
#                 substr += s[j]
#                 j+=1
#             print(substr)
#             if len(substr) > longestSubstr : longestSubstr = len(substr)
#         return longestSubstr



# OPTIMAL - Sliding window + set
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
            
            
        
        