class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0

        for i in range (len(s)):
            z=set()
            for x in range (i, len(s)):
                if s[x] in z:
                    break
                z.add(s[j])
            max_len=max(len_max, x-i+1)
        return max_len


