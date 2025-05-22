class Solution {
 public:
  struct Position {
    int x;
    int y;
  };

  bool bfs(const vector<vector<char>>& board, string_view word,
           const int startX, const int startY) const {
    const int m = board.size();
    const int n = board[0].size();
    vector<vector<uint8_t>> isVisited(m * n, 0);
    struct Node {
      int x;
      int y;
      string_view::const_iterator wordIndex;
    };
    std::deque<Node> candidates;
    candidates.push_back({startX, startY, word.cbegin()});
    while (!candidates.empty()) {
      const auto [x, y, it] = candidates.front();
      candidates.pop_front();
      if (x == -1 || y == -1 || x >= m || y >= n || isVisited[x][y] == 1) {
        continue;
      }
      isVisited[x][y] = 1;
      if () }
  }

  bool dfs(const vector<vector<char>>& board, string_view word,
           const int startX, const int startY,
           string_view::const_iterator it) const {}

  bool exist(vector<vector<char>>& board, string word) {
    const int m = board.size();
    const int n = board[0].size();
    vector<vector<uint8_t>> isVisited(m * n, 0);
    vector<Position> frontPositions;
    vector<Position> backPositions;
    for (int i = 0; i != m; ++i) {
      for (int j = 0; j != n; ++j) {
        if (board[i][j] == word.front()) {
          frontPositions.push_back({i, j});
        }
        if (board[i][j] == word.back()) {
          backPositions.push_back({i, j});
        }
      }
    }
    if (frontPositions.empty() || backPositions.empty()) {
      return false;
    }
    if (backPositions.size() < frontPositions.size()) {
      std::swap(backPositions, frontPositions);
      std::reverse(word.begin(), word.end());
    }
    std::deque<Position> candidates;
    candidates.push_back(frontPositions.back());
    frontPositions.pop_back();
    while (!candidates.empty()) {
      const auto [x, y] = candidates.front();
      candidates.pop_front();
      isVisited[x][y] = 1;
    }
  }
};