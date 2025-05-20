class Solution {
 public:
  int maxSubArray(vector<int>& nums) {
    int maxSum = nums.front();
    int sum = 0;
    for (const auto n : nums) {
      sum += n;
      maxSum = std::max(sum, maxSum);
      if (sum < 0) {
        sum = 0;
      }
    }
    return maxSum;
  }
};