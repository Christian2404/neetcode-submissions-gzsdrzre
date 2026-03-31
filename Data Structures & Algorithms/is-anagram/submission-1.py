class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == 0 | len(t) == 0:
            return False

        if len(s) != len(t): # Not anagram unless same length
            return False

        # Iterate through s and t

        s_characters = {}
        t_characters = {}

        for i in range(len(s)):
            if s[i] not in s_characters:
                s_characters[s[i]] = 1
            else: 
                s_characters[s[i]] += 1

            if t[i] not in t_characters:
                t_characters[t[i]] = 1
            else: 
                t_characters[t[i]] += 1

        if s_characters == t_characters:
            return True

        else:
            return False

    

        