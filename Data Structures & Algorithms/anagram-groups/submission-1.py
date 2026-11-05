class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = {}

        for i, s in enumerate(strs):

            key = "".join(sorted(s)) # sort each word, sorted() splits string into an array so .join must be used to merge it back into a single string

            if key not in words:
                words[key] = [s]

            else:
                words[key].append(s)

        return list(words.values())