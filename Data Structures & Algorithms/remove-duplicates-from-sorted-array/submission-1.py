class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        
        k = 1
        n = len(nums)

        if n == 0:
            return 0

        prev = nums[0]

        for i in range(1, n):
            if nums[i] != prev:
                nums[k] = nums[i]
                prev = nums[i]
                k+=1

        return k

             