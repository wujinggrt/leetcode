class Solution {
 public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    const int m = matrix.size();
    const int n = matrix[0].size();
    std::vector<int> spiral(m * n);
    enum Direction : int { Right = 0, Down = 1, Left = 2, Up = 3 };
    Direction d = Right;
    int i = 0;
    int j = 0;
    int steps = 1;
    int horizontal_steps = n;
    int vertical_steps = m - 1;
    for (int& element : spiral) {
      element = matrix[i][j];
      if ((d == Left || d == Right) && steps == horizontal_steps) {
        steps = 0;
        --horizontal_steps;
        d = d == Right ? Down : Up;
      } else if ((d == Down || d == Up) && steps == vertical_steps) {
        steps = 0;
        --vertical_steps;
        d = d == Down ? Left : Right;
      }
      switch (d) {
        case Right: {
          ++j;
          break;
        }
        case Down: {
          ++i;
          break;
        }
        case Left: {
          --j;
          break;
        }
        case Up: {
          --i;
          break;
        }
      }
      ++steps;
    }
    return spiral;
  }
};