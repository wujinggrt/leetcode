class Solution {
 public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    /*
     * 使用双端队列，队列保存index，且队首是最大值。
     * 队列是单调递减的,每次添加元素只能从尾部添加，
     * 有违反顺序的元素的时候，pop所有比当前元素小的元素。
     * 我们需要的只是最大值，所以不会对结果影响。
     */
    const int n = nums.size();
    deque<int> q;
    // 预处理第一个window前的元素
    for (int i = 0; i != k - 1; ++i) {
      while (!q.empty() && nums[i] >= nums[q.back()]) {
        // 弹出违反大小顺序
        q.pop_back();
      }
      q.push_back(i);
    }
    vector<int> ans;
    for (int i = k - 1; i != n; ++i) {
      while (!q.empty() && nums[i] >= nums[q.back()]) {
        q.pop_back();
      }
      q.push_back(i);
      // 弹出窗口外元素
      while (q.front() <= i - k) {
        q.pop_front();
      }
      ans.push_back(nums[q.front()]);
    }
    return ans;
  }
};