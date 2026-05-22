class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) == 0:
            return False

        prev = nums[0]

        for i in range(1, len(nums)):
            if prev in nums[i:]:
                return True
            prev = nums[i]

        return False