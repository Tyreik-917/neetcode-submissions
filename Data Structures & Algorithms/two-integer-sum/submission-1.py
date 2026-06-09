class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, val in enumerate(nums):

            find = target - val

            if find in hashmap:
                return [hashmap[find], idx]

            else:
                hashmap[val] = idx