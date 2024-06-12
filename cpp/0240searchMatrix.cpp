class Solution {
 public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int i = 0;
    int j = matrix[0].size() - 1;
    while (j >= 0 && i < matrix.size()) {
      const int root = matrix[i][j];
      if (root > target)
        --j;  // 向左
      else if (root < target)
        ++i;  // 向右
      else
        return true;
    }
    return false;
  }
};