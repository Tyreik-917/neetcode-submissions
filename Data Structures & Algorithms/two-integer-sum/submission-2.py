class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, val in enumerate(nums):
            
            find = target - val

            if find not in hashmap:
                hashmap[val] = idx

            else:
                return [hashmap[find], idx]