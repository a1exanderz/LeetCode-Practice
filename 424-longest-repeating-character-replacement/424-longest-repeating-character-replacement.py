class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # AABABBA
        # BBAAAAB 3
        # AADDDAA k=2

        # valid window: windowLen - mostFreqChar <= k
        # As long as the window is valid, continue to expand our window
        # Else shift left pointer until string becomes valid again
        
        count = {}
        output = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            output = max(output, r - l + 1)
            
        return output
        
#         ### My solution ### Time limit exceeded
#         while l <= r and r < len(s) + 1:
#             windowLen = r - l
            
#             freqCharCount = 1
#             for char in s[l:r]:
#                 if char in count.keys():
#                     count[char] += 1
#                     freqCharCount = max(freqCharCount, count[char])
#                 else:
#                     count[char] = 1
            
#             # print("l", l, "r", r, s[l:r])
#             # print("wL", windowLen, "fCC", freqCharCount)
            
#             if windowLen - freqCharCount <= k:
#                 r += 1
#                 output = max(output, windowLen)
#             else:
#                 l += 1
                
#         return output
        