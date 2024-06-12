class Solution {
  int char_to_index(const char c) { return c - 'a'; }

 public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size()) {
      return false;
    }
    std::array<int, 26> repeats{};
    for (const char c : s) {
      ++repeats[c - 'a'];
    }
    for (const char c : t) {
      if (--repeats[c - 'a'] < 0) {
        return false;
      }
    }
    return true;
  }
};