class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Iterate through strings, for each string sort and add to map

        word_map = {}

        for word in strs:

            sorted_chars = sorted(word)
            sorted_word = "".join(sorted_chars)

            if sorted_word in word_map:
                word_map[sorted_word].append(word)

            else:
                word_map[sorted_word] = [word]

        # Iterate through map and return a new list

        res = []

        for key in word_map:
            res.append(word_map[key])

        return res