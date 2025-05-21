class Solution {
    public:
        bool canJump(vector<int>& nums) {
            int farthest = -1;
            for (int i = 0; i != nums.size(); ++i) {
                farthest = std::max(farthest, nums[i] + i);
                if (farthest == i) {
                    return false;
                }
            }
            return true;
        }
};