class Solution {
    public:
     struct Position {
       int x;
       int y;
     };
   
     bool dfs(const vector<vector<char>>& board, vector<vector<char>>& isVisited,
              const int x, const int y,
              string::const_iterator it, string::const_iterator end) const {
       if (it == end) {
           return true;
       }        
       const int m = board.size();
       const int n = board[0].size();
       if (x == -1 || y == -1 || x == m || y == n || isVisited[x][y] == '#' || board[x][y] != *it) {
           return false; // reached boundary or mismatched
       }
       isVisited[x][y] = '#';
       bool isMatched = dfs(board, isVisited, x - 1, y, it + 1, end);
       if (!isMatched) isMatched = dfs(board, isVisited, x + 1, y, it + 1, end);
       if (!isMatched) isMatched = dfs(board, isVisited, x, y - 1, it + 1, end);
       if (!isMatched) isMatched = dfs(board, isVisited, x, y + 1, it + 1, end);
       isVisited[x][y] = '*';
       return isMatched; 
       }
   
     bool exist(vector<vector<char>>& board, string word) {
       const auto m = board.size();
       const auto n = board[0].size();
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
       vector<vector<char>> isVisited(m, vector<char>(n, '*'));
       for (const auto& pos: frontPositions) {
           if (dfs(board, isVisited, pos.x, pos.y, word.cbegin(), word.cend())) {
               return true;
           }
       }
       return false;
     }
   };