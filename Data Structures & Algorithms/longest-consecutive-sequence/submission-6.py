class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxList = 0
        for num in numSet:
            if(num-1) not in numSet:
                length = 1
                maxList = max(length, maxList)
                while(num + length) in numSet:
                    length+=1
                    maxList = max(length, maxList)
        return maxList
