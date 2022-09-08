class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Each anagram has its own equivalent hashTable
        # Nested hashTables?
        # The key is a hashTable, and values are strings that match that hashTable
        # Then, append all values of each key in the main hashTable into output
        
        mainTable = {}
        # Create a temporary hashTable for each string in the array
        for string in strs:
            tempTable = {}
            for c in string:
                if c in tempTable.keys():
                    tempTable[c] += 1
                else:
                    tempTable[c] = 1

            # tempItems = frozenset(tempTable.items())

            if frozenset(tempTable.items()) not in mainTable.keys():
                mainTable[frozenset(tempTable.items())] = [string]
            else:
                mainTable[frozenset(tempTable.items())].append(string)
        
        return mainTable.values()
        
    
        ######## Solution without a nested hashTable #######
        # Create a count array that has 26 blanks for each letter, for each string
        # Add the count array to a main hashTable if new, otherwise append
        
#         mainTable = {}
        
#         for string in strs:
#             countArray = [0] * 26
#             for c in string:
#                 countArray[ord(c) - ord('a')] += 1
            
#             if tuple(countArray) not in mainTable.keys():
#                 mainTable[tuple(countArray)] = [string]
#             else:
#                 mainTable[tuple(countArray)].append(string)       
                
#         return mainTable.values()
        
        