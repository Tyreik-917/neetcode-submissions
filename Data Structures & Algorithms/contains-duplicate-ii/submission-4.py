class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        i = 0
        j = 1

        while j < len(nums):
            while abs(i - j) > k:
                i += 1

            temp_i = i
            while temp_i < j:
                if nums[temp_i] == nums[j]:
                    return True
                temp_i += 1

            j+=1

        return False