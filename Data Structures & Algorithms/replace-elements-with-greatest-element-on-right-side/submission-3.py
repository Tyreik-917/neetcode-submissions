class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        val = 0

        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])

        return arr[:len(arr)-1] + [-1]

        

            