#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_set<int> seen;

        // Iterate through the array and check if elems in set
        for (int num : nums) {
            
            if (seen.find(num) != seen.end()) {
                return true; // Duplicate found!
            }

            seen.insert(num);
        }

        return false; // No duplicates in array
    }
};