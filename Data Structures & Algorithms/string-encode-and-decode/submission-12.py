class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for phase in strs:
            s+= str(len(phase)) + "#" + phase
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            strs.append(s[j+1 :j + 1 + length])
            i = 1 + j + length

        return strs


