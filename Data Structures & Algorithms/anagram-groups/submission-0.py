class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        newdict = {}

        for str in strs:
            key = "".join(sorted(str))

            if key not in newdict:
                newdict[key] = []

            newdict[key].append(str)

        return list(newdict.values())