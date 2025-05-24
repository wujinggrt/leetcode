class Solution {
  static constexpr int DIRS[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

 public:
  vector<vector<int>> generateMatrix(int n) {
    vector ans(n, vector<int>(n));
    int i = 0, j = 0, di = 0;
    for (int val = 1; val <= n * n; val++) {
      ans[i][j] = val;
      int x = i + DIRS[di][0];
      int y = j + DIRS[di][1];
      if (x < 0 || x >= n || y < 0 || y >= n || ans[x][y]) {
        di = (di + 1) % 4;
      }
      i += DIRS[di][0];
      j += DIRS[di][1];
    }
    return ans;
  }
};