## TODO
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5
- [ ] 6
- [ ] 7

注意，与 C++ 不同，Python 中，负数取模与正数不同，取模结果为正数，结果为对应的模的数的补数。比如 -17 % 10 得到 3，如果想要 7，应当用 10 减去负数取模结果。在负整数的整数除法中，会向下取整，比如 -17 // 10 得到 -2，而不是 -1，可以看到整数除法都是向下取整。如果想要达到与 C++ 相同效果，那么负数的整数除法和取模应当调整如下：

```py
digit = 0 if x % 10 == 0 else x % 10 - 10
n = (n - digit) // 10
```

- [ ] 8
- [ ] 10 字符串匹配

```py
  # dp，状态：f[i][j] 表示 s 前 i 字符与 p 前 j 字符匹配
  # 转移方程如下，根据 p[j]：
  # matches(x, y) 判断两字符是否匹配，或者 y 是 .
  # p[j] 为 *，f[i][j] = f[i-1][j] or f[i][j-2] if matches(s[i], p[j-1]) else f[i][j-2]
  # p[j] 为 小写字符或 ., f[i][j] = f[i-1][j-1] if matches(s[i], p[j]) else False
  # 解释：
  # 1. 当 p[j] 为 *, 第 j-1 个字符匹配 0 次，即不匹配情况下，把 p 的匹配在 j-1 j 处当 0 次匹配。
  #    于是，f[i][j] = f[i][j-2]
  # 2. 匹配 1,2,3... 次情况下，有 f[i][j] = f[i-1][j-2] if s[i]==p[j-1]
  #    f[i][j] = f[i-2][j-2] if s[i-1]==s[i]==p[j-1], ...
  #    如此编程比较麻烦，所以把匹配 1,2,3... 次当做 + 的语义考虑，本质为两种情况：
  #    p[j] 相当于 +，s[i] 与 p[j-1] 匹配之后，
  #    1) 考察 s[i-1] 是否继续进行匹配 p[0..j], 消去了最后一个s[i]影响，此时为 True，
  #       考察前面情况，对应 f[i-1][j], 如此递归地直到 + 只匹配一个的情况。
  #    2) 如果不能匹配，放弃匹配，当做 + 只匹配到 1 个字符的情况，此时为 True，于是参考前面是否匹配，
  #       即可对应 f[i][j-2]，把 p 中 j-1 和 j 字符当做
  #       0 次匹配处理
  #    f[i][j] = (f[i-1][j] or f[i][j-2]) if s[i]==p[j-1] else f[i][j-2]
```

- [ ] 11

复杂的双指针。

- [ ] 12
- [ ] 14
- [ ] 15
- [ ] 16
- [ ] 17
- [ ] 19
- [ ] 20
- [ ] 22

关注 dfs 和 backtrack.

- [ ] 23
- [ ] 24
- [ ] 25
- [ ] 31 next permutation

## 31 next permutation
思路偏记忆。具体如如：12465的下一个应该是123564
1.应该从右向左找数组A，下标为i；
2.在第一个A[i-1] > A[i]的数，然后在和左边第一个比i小的数交换，这样才能得到下一个比当前大的数。
3.将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，因为升序排列就是最小的排列，也就是那一部分的站在高位的数尽可能小。

## 32 最长有效括号：DP 和哨兵思路

Tag：栈 (最优)，DP

最佳思路为使用栈。遍历时可以根据过往来判断当前是否有效。记录有效匹配括号数量即可。

巧妙设计和见解：开始前令栈底预先保存一个 '(' 下标 -1，作为哨兵。用于检查遇到的第一个不匹配的 ')'，及时处理和重新清零计数。设置新的哨兵，检查下一个不匹配的 ')'。

这是非常值得学习的思路。使用**哨兵思路**或占位，一般多设计一个匹配对应目标的对象，方便检测。哨兵可以方便地检查第一个出现不匹配，或者推广来说，检查第一个出现异常的地方。妥当处理。

遍历到 '(' 时，将下标入栈。遍历到 ')' 时，直接弹栈。弹栈后，
- 如果栈非空，那么栈顶的元素下标是未匹配的左括号，记为 v。即当前括号 ')' 下标为 m。于是有区间 (v, m] 匹配到括号。当前有效括号数量是 m - v 个。
- 如果栈空，说明弹出了哨兵，代表当前有括号不匹配。于是把当前下标作为哨兵，再次入栈。

洞察栈的**规律**。用不同方法表达，可以优化空间复杂度到 O(1)。不使用栈，使用两个计数器即可。栈中总是保存 "("，内容是 "((((...("，有**冗余**，有规律和优化空间。每当匹配到 ")" 时逐个弹出。当 ")" 数量过多，匹配不到 "("，便认为无效。

最后的方案：使用两个变量模拟如此关系的栈。需要从左往右扫描，也需要从右往左扫描。
- 从左往右扫描时，以 left 必须大于等于 right。否则右侧括号，找不到左括号来匹配。 但是，从左往右扫描，会漏掉一种情况。比如 "()(()" 总是满足 left >= right，但长度是 2 所以需要从右扫描一遍。
- 从右向左扫描。一左一右，将两个情况左右限制在最大值上。

## 33 搜索旋转排序数组：

数组有序，但是可能向左或向右 rotate 了。比如 [4 5 6 7 0 1 2]。

使用二分查找。二分后，得到 mid，需要确定，值是在 mid 的左侧还是右侧。考虑**状态机**。我们定义跨越点下标 leap 是最小值点，且此最小值左最大值。如果不存在如此的值，那么数组单调增加。如果 nums[0] < nums[-1]，代表使用二分查找即可。或是用哨兵思想，在左侧插入无穷大，但是复杂化了。二分区间 [left:right] 时，下标 mid 有如下情况：
- 情况 1：nums[left] > nums[mid]。跨越点在 mid 左侧区间 [left, mid)，数组单调递增序列包含 [left:leap] 和 [leap:mid] [mid:right]。
- 情况 2：nums[left] < nums[mid] and nums[right-1] < nums[mid]，跨越点在 mid 右侧区间 [mid:right]。单调递增区间包含 [left:mid], [mid:leap] 和 [leap:right]。
- 情况 3：nums[left] < nums[mid] and nums[mid] < nums[right-1]，区间有序，无跨越点。执行二分即可。

有了上面信息，便逐渐收缩 left 和 right，锁定 target 所在区间。当发现有三个递增区间时，不能像二分直接找下一个区间，放宽条件，到可能存在数的区间即可。由于 leap 下标未知，为了简洁，判断 target 是否在已知的单个单调的区间更方便。

[python code](./py/0033.py)

- [ ] 34
- [ ] 39
- [ ] 40
- [ ] 41
- [ ] 43
- [ ] 44
- [ ] 45
- [ ] 46
- [ ] 47
- [ ] 48
- [ ] 49
- [ ] 50
- [ ] 51
- [ ] 53
- [ ] 54
- [ ] 55
- [ ] 56
- [ ] 57
- [ ] 59
- [ ] 60
- [ ] 61
- [ ] 62
- [ ] 63
- [ ] 64
- [ ] 70
- [ ] 72
- [ ] 74
- [ ] 75
- [ ] 76
- [ ] 78
- [ ] 79
- [ ] 81
- [ ] 82
- [ ] 84
- [ ] 85
- [ ] 86
- [ ] 88
- [ ] 91
- [ ] 92
- [ ] 93
- [ ] 95
- [ ] 96
- [ ] 97
- [ ] 98
- [ ] 99
- [ ] 101
- [ ] 102
- [ ] 103
- [ ] 104
- [ ] 105
- [ ] 106
- [ ] 110
- [ ] 111
- [ ] 112
- [ ] 113
- [ ] 114
- [ ] 115
- [ ] 120
- [ ] 121
- [ ] 122
- [ ] 123
- [ ] 124
- [ ] 127
- [ ] 128
- [ ] 129
- [ ] 130
- [ ] 131
- [ ] 132
- [ ] 135
- [ ] 136
- [ ] 138
- [ ] 139
- [ ] 140
- [ ] 142
- [ ] 143
- [ ] 144
- [ ] 145
- [ ] 146
- [ ] 148
- [ ] 152
- [ ] 154
- [ ] 155
- [ ] 160
- [ ] 162
- [ ] 164
- [ ] 165
- [ ] 169
- [ ] 174
- [ ] 179
- [ ] 188
- [ ] 198
- [ ] 199
- [ ] 200
- [ ] 206
- [ ] 207
- [ ] 208
- [ ] 209
- [ ] 211
- [ ] 212
- [ ] 213
- [ ] 215
- [ ] 221
- [ ] 222
- [ ] 224
- [ ] 226
- [ ] 227
- [ ] 230
- [ ] 233
- [ ] 234
- [x] 236 lowestCommonAncestor
- [x] 239 maxSlidingWindow

使用双端队列，队列内容保存数组的下标，对应的元素满足单调递减的关系，队首对应当前窗口的最大值。每次添加元素只能从尾部添加， 有违反顺序的元素的时候，pop所有比当前元素小的元素。 我们需要的只是最大值，所以不会对结果影响。
- [x] 240 searchMatrix # 使用二分查找不合适，用二叉树的思路。此题不够熟悉

将矩阵逆时针旋转45度，可以得到类似二叉树的结构。我们记矩阵中，右上角的元素为root。我们从根开始处理，根的下标为(i,j)=(0,n-1)，其中左分支元素变小，对应下标j--，右分支元素变大，对应下表i++。当：
  1. root > target ，则 target 一定在 root 所在矩阵的列的左侧，执行--j。
  2. root < target ，则 target 一定在 root 所在矩阵的列的右方，即 root 所在列可被消去，执行++i。
  3. root==target，返回true。若最后无结果，返回false。

insights在于：简单的在各行或列二分搜索，会各自遗漏列和行的顺序，。我们可以进一步观察规律，横纵行不通，考虑逆时针旋转45度后，按照二叉树的方式处理。
- [x] 242 isAnagram
简单的使用数组替代哈希，统计出现次数后再比较。
- [x] 264

转移方程：dp[i]=min(dp[p_2]*2,dp[p_3]*3,dp[p_5]*5)。p2,p3,p5分别是丑数序列的下标，用于递推丑数序列。由于丑数需要满足递增，所以 更新序列时候，从p2,p3,p5指向的丑数中，分别乘以2，3，5，选取最小值作为更新， 并将对应的下标自增，移动到下一个下标。
- [ ] 275
- [ ] 279
- [ ] 287
- [ ] 295
- [ ] 297
- [ ] 300
- [ ] 309
- [ ] 312
- [ ] 313
- [ ] 315
- [ ] 316
- [ ] 321
- [ ] 322
- [ ] 327
- [ ] 328
- [ ] 329
- [ ] 336
- [ ] 337
- [ ] 343
- [ ] 347
- [ ] 349
- [ ] 354
- [ ] 357
- [ ] 363
- [ ] 377
- [ ] 381
- [ ] 382
- [ ] 384
- [ ] 394
- [ ] 398
- [ ] 402
- [ ] 403
- [ ] 406
- [ ] 407
- [ ] 410
- [ ] 416
- [ ] 438
- [ ] 440
- [ ] 443
- [ ] 445
- [ ] 450
- [ ] 452
- [ ] 454
- [ ] 458
- [ ] 463
- [ ] 468
- [ ] 470
- [ ] 473
- [ ] 474
- [ ] 480
- [ ] 486
- [ ] 494
- [ ] 498
- [ ] 504
- [ ] 509
- [ ] 514
- [ ] 516
- [ ] 518
- [ ] 523
- [ ] 538
- [ ] 543
- [ ] 560
- [ ] 567
- [ ] 583
- [ ] 647
- [ ] 654
- [ ] 662
- [ ] 673
- [ ] 677
- [ ] 678
- [ ] 679
- [ ] 692
- [ ] 695
- [ ] 698
- [ ] 704
- [ ] 714
- [ ] 718
- [ ] 739
- [ ] 752
- [ ] 761
- [ ] 845
- [ ] 862
- [ ] 871
- [ ] 879
- [ ] 887
- [ ] 895
- [ ] 912
- [ ] 922
- [ ] 941
- [ ] 958
- [ ] 973
- [ ] 1044
- [ ] 1095
- [ ] 1114
- [ ] 1122
- [ ] 1143
- [ ] 1160
- [ ] 1206
- [ ] 1207
- [ ] 1312
- [ ] 1339
- [ ] 1356
- [ ] 1365
- [ ] 1373
- [ ] 1379
- [ ] 1382
- [ ] 1420
- [ ] 1423
- [ ] 1449
- [ ] 1877
- [ ] 1996
- [ ] 2058
- [ ] 3156
- [ ] 3613
- [ ] 4387