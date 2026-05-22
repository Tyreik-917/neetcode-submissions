class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        n = len(nums)

        while i < n:
            
            if nums[i] == val:
                nums.pop(i)
                i-=1
                n-=1

            i+=1
            k+=1

        return k
