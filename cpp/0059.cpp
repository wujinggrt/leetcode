class Solution {
 public:
  vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> spiral(n, vector<int>(n));
    int i = 0;
    int j = 0;
    int horizontal_count = n;
    int vertical_count = n - 1;
    int visited_count = 0;
    // 0 for right, 1 for down, 2 for left, and 3 for up
    int direction = 0;
    for (int num = 1; num <= n * n; ++num) {
      spiral[i][j] = num;
      ++visited_count;
      if (direction % 2 == 0 && visited_count == horizontal_count) {
        --horizontal_count;
        visited_count = 0;
        direction = (direction + 1) % 4;
      } else if (direction % 2 == 1 && visited_count == vertical_count) {
        --vertical_count;
        visited_count = 0;
        direction = (direction + 1) % 4;
      }
      switch (direction) {
        case 0:
          ++j;
          break;
        case 1:
          ++i;
          break;
        case 2:
          --j;
          break;
        case 3:
          --i;
          break;
      }
    }
    return spiral;
  }
};