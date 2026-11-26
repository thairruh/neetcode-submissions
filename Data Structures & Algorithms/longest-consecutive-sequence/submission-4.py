class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)

        max_length = 0

        for i in hashset:
            if i - 1 not in hashset:
                total = 1
                while i + 1 in hashset:
                    total += 1
                    i += 1
                if total > max_length:
                    max_length = total

        return max_length

