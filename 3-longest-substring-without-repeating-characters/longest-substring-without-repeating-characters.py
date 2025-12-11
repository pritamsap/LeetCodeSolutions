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
        output = 0
        charSet = set()
        maxLength = 0
        r = 0
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while l < r and s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                charSet.remove(s[l])
                l += 1

            if s[r] not in charSet:
                charSet.add(s[r])
            length = (r - l) + 1
            maxLength = max(maxLength, length)
            r += 1

        return maxLength
            


        