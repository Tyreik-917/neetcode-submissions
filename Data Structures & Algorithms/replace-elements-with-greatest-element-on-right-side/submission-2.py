class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_arr = []
        val = 0

        for i in range(len(arr)-1):
            val = max(arr[i+1:])
            new_arr.append(val)

        return new_arr + [-1]

        

            