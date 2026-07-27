class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            find = target - nums[i]

            if find not in hashmap:
                hashmap[nums[i]] = i

            else:
                return [hashmap[find], i]
