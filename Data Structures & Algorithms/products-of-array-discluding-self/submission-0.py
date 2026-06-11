class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = postfix = 1

        for i in range(len(nums)):

            res[i]*= prefix
            res[len(res)-1 - i]*=postfix
            prefix*=nums[i]
            postfix*=nums[len(nums) - 1 - i]

        return res


        