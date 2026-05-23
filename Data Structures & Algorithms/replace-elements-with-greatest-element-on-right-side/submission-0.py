class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        


        for i in range(len(arr)-1):

            val = 0

            for j in range(i+1, len(arr)):
        
                if val < arr[j]:
                    val = arr[j]

            arr[i] = val
        
        arr[len(arr)-1] = -1
        return arr

            