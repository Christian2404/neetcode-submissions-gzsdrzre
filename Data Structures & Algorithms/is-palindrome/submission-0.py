class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = (s.replace(' ', '')).lower() # Convert to lowercase & remove all spaces.
        s = "".join(char for char in s if char.isalnum())

        # Create two pointers from centre, move outward and if != return false if reach end, return True 

        if len(s) % 2 == 0: # If divisible by two 
            l = int((len(s) / 2) - 1)
            r = int((len(s) / 2))
        else: # Ignore middle character | len = 11 middle 0 -> 11 (i = 12) 13 -> 24
            l = int(((len(s) - 1) / 2) - 1)
            r = int(((len(s) - 1) / 2) + 1)

        while l >= 0: # l and r are equidistant from bounds and move at same speed 
            if s[l] != s[r]: # Left and right character not the same
                return False

            else: # Check next character  
                l -= 1
                r += 1

        return True 



