class Solution {
 public:
  vector<vector<int>> insert(vector<vector<int>>& intervals,
                             vector<int>& newInterval) {
    auto left =
        std::lower_bound(intervals.begin(), intervals.end(), newInterval[0],
                         [](const auto& interval, const int start) {
                           return interval[1] < start;
                         });
    auto right = std::upper_bound(
        left, intervals.end(), newInterval[1],
        [](const int val, const auto& interval) { return val < interval[0]; });
    if (left != intervals.end()) {
      newInterval[0] = std::min((*left)[0], newInterval[0]);
    }
    if (right != intervals.begin()) {
      newInterval[1] = std::max((*(right - 1))[1], newInterval[1]);
    }
    intervals.insert(intervals.erase(left, right), newInterval);
    return intervals;
  }
};