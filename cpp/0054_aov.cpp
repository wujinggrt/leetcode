class Solution {
 public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    // 分析，使用下标i, j记录当前位置，下一位置需要先确定方向规律和顺序如下：
    // 右：(i, j + 1)， 下：(i + 1, j)，左：(i, j - 1)，上：(i + 1, j)
    // 再使用一个值来记录边界，水平的边界初始值为row，垂直则为column，
    // 当水平方向和垂直方向走到头一次后，边界就--，并且换方向，直到完成所有count
    int i = 0;
    int j = 0;
    int horizontal = matrix[0].size();  // boundary
    int vertical = matrix.size() - 1;
    enum Direction { right = 0b1, down = 0b10, left = 0b100, up = 0b1000 };
    Direction direction = right;
    vector<int> spiral(matrix.size() * matrix[0].size());
    int step = 0;
    for (int& element : spiral) {
      ++step;
      element = matrix[i][j];
      if (((direction & (right | left))) && (step == horizontal)) {
        step = 0;
        direction = (Direction)((direction << 1) % 15);  // 8 % 7 == 1
        horizontal--;
      } else if (((direction & (up | down))) && (step == vertical)) {
        step = 0;
        direction = (Direction)((direction << 1) % 15);
        vertical--;
      }
      switch (direction) {
        case right:
          ++j;
          break;
        case down:
          ++i;
          break;
        case left:
          --j;
          break;
        case up:
          --i;
          break;
      }
    }
    return spiral;
  }
};