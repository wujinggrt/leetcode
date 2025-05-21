class Solution {

    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            std::sort(intervals.begin(), intervals.end());
            vector<vector<int>> nonOverlapped{intervals.front()};
            for (int i = 1; i != intervals.size(); ++i) {
                auto& slice = nonOverlapped.back();
                if (slice[1] >= intervals[i][0]) {
                    slice[1] = std::max(intervals[i][1], slice[1]);
                } else {
                    nonOverlapped.push_back(intervals[i]);
                }
            }
            return nonOverlapped;
        }
    };