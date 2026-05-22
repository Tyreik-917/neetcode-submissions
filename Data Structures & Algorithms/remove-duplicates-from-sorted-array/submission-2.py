class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1
        i = 0

        size = len(nums)

        while i != size:
            if nums[i] in nums[k:]:
                nums.pop(i)
                size = size - 1
 
            else:
                k = k + 1
                i = i + 1

        return k
