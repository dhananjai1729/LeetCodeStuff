// Answer to https://leetcode.com/problems/remove-element
// Amal George M
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto itrEnd = std::remove(nums.begin(), nums.end(), val);
        auto pos = std::distance(nums.begin(),itrEnd);
        return (static_cast<int> (pos));
    }
};
