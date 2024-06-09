class Solution {
  bool walkThroughForBuilding(vector<TreeNode*>& path, TreeNode* root,
                              TreeNode* target) {
    // 假设root已经被放入了path，通过回溯来决定是否pop_back
    if (!root) {
      return false;
    }
    if (root == target) {
      return true;
    }
    if (root->left) {
      path.push_back(root->left);
      if (walkThroughForBuilding(path, root->left, target)) {
        return true;
      }
      path.pop_back();
    }
    if (root->right) {
      path.push_back(root->right);
      if (walkThroughForBuilding(path, root->right, target)) {
        return true;
      }
      path.pop_back();
    }
    return false;
  }

 public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    vector<TreeNode*> p_path;
    vector<TreeNode*> q_path;
    p_path.push_back(root);
    q_path.push_back(root);
    walkThroughForBuilding(p_path, root, p);
    walkThroughForBuilding(q_path, root, q);
    const int min_len = min(p_path.size(), q_path.size());
    for (int i = 0; i < min_len; ++i) {
      if (p_path[i] != q_path[i]) {
        return p_path[i - 1];
      }
    }
    return p_path[min_len - 1];  // 返回较小者的最后一个
  }
};