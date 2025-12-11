class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # longest substring without duplicate charaters
        # sliding window with pointers
        # use pointer L and R, use a set to store non dup values
        # use max to store the biggest substring
        # l = 0, r = 0
        # temp = set() 
        # if char not in set r += 1
        # if char in set, max(currentLength, maxLength)
        # l += 1, remove the duplicate char

        # l = 0
        # r = 0

        # tmmzuxt
        # l r
        # mzuxt
        # set = [tmzux]


        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, (r-l)+1)
        return res
            


        