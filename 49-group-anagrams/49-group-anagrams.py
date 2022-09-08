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
        
        # Append each key's value to an output array
        output = []
        for key in mainTable:
            output.append(mainTable[key])
            
        return output
        
        