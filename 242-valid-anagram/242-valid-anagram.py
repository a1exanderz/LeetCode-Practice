class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictOne = {}
        dictTwo = {}
        
        for c in s:
            if ord(c) in dictOne.keys():
                dictOne[ord(c)] += 1
            else:
                dictOne[ord(c)] = 1
                
        for c in t:
            if ord(c) in dictTwo.keys():
                dictTwo[ord(c)] += 1
            else:
                dictTwo[ord(c)] = 1
                
        return dictOne == dictTwo