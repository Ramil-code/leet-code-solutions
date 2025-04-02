class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0

        for i in range (len(s)):
            added=set()
            
            for x in range (i, len(s)):
                if s[x] in added:
                    break
                added.add(s[x])
                max_len=max(max_len,i-x+1)
        
        return max_len