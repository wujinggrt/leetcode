// 最优解
class Solution {
 public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) {
      // 其中之一是root，立即返回
      // 或者是递归时遇到了p或q，立即返回。此时有两种情况。
      // 1）如果另一个节点在root的子树，那么root就是lowest公共祖先，在递归时候，
      // 其他分支节点都不会包含p和q，都是nullptr，此root能够确保返回给最外层调用。
      // 2）如果另一个节点不在root的子树，那么当前解决不了，只能抛给上一层调用者查看。
      // 此题保证了p和q会存在树中，所以不会出现最终返回的根不包含两个节点情况。此corner
      // case无需考虑。
      return root;
    }
    auto* left = lowestCommonAncestor(root->left, p, q);
    auto* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) {
      return root;  // 分别分布在两侧，是我们想要的结果
    }
    // 如果当前root下，1）左右子树不包含p或q，会返回nullptr
    // 2）如果仅仅包含一个，那么此root还不是公共祖先，返回即可，回溯给caller处理。
    return left ? left : right;
  }
};
#if 0
// 次优解
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
#endif