class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+ 1)] # creates an array of arrays, where each index represents the frequency associated with the values

        for n in nums:
            count[n] = 1 + count.get(n, 0) # add one to the current count associated with n
        for n, cnt in count.items(): # for each key value pair in count
            freq[cnt].append(n) # add n to the index associated with its count

        res = [] # new array storing the k most frquent values

        # loop backwards becase we want to start with most frequent
        for arr in reversed(freq): # accesses each array
            for n in arr: # accesses each element inside the array
                res.append(n) 
                
                if len(res) == k:
                    return res



