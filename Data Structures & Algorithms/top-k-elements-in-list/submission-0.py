class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        most_freq = []

        for f in range(0, k):
            max_key = max(freq, key=freq.get)
            most_freq.append(max_key)
            freq.pop(max_key)

        return most_freq