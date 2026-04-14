class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        # Build arr of s1
        s1_chars = [0] * 26
        for char in s1:
            s1_chars[ord(char) - ord('a')] += 1

        # Build inital arr of s2
        s2_chars = [0] * 26
        for i in range(len(s1)):
            s2_chars[ord(s2[i]) - ord('a')] += 1

        # Iterate through fixed window s2 and compare to s1 arr
        for i in range(1, len(s2) - len(s1) + 1):

            if s1_chars == s2_chars:
                return True 

            s2_chars[ord(s2[i - 1]) - ord('a')] -= 1
            s2_chars[ord(s2[(i + len(s1) - 1)]) - ord('a')] += 1

            print(s1_chars, s2_chars)

        return s1_chars == s2_chars