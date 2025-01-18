class Solution {

    // min heap
    /**
     * ugly number是质数分解中，只包含2，3，5的数。比如8=2*2*2，
     * 小顶堆中，堆顶元素为x，则x是堆中最小的丑数。又2，3，5倍的x也是丑数，
     * 所以也要进一步将2*x,3*x,5*x加入堆。但是堆中的元素很有可能已经出现的重复元素。
     * 再使用一个set，保证独一。
     */
    int minHeap(int n) {
        priority_queue<long, vector<long>, greater<long>> heap;
        set<long> accounted;
        heap.push(1L);
        accounted.insert(1L);
        int ugly = 0;
        for (int i = 0; i < n; ++i) {
            const long num = heap.top();
            heap.pop();
            ugly = static_cast<int>(num);
            for (int factor: {2, 3, 5}) {
                const long next = factor * num;
                if (!accounted.contains(next)) {
                    accounted.insert(next);
                    heap.push(next);
                }
            }
        }
        return ugly;
    }

    /**
     * 每个丑数都可以由其他较小的丑数乘以2，3或5来得到，这是递归地定义。base
case是1，不断向前推导。
     * 起初，丑数序列为1，1-3轮添加元素如下：
     * 1:[1,2,3,5]; 2: 在1的基础上加入4,6,10; 3: 添加6,9,15。
     * 比如一二轮中，4如何放到3和5之间。使用堆保存，则需要处理重复和维护堆。
     * 小顶堆占用空间较多。我们可以用动态规划来优化。
     * dp思路如下，使用三个指针p2,p3,p5,分别指向**当前丑数**的下一个递推。
     * 起初，p2,p3,p5都指向第一个数，1，随后，从这些数中，找到最小的数，再根据最小的丑数来推进下一个递推。
     * 因为丑数序列是递增的，所以我们不断更新，从上一个p2,p3,p5中选择最小的来放到当前位置，再更新指针。
     *
     * 转移方程：dp[i]=min(dp[p_2]*2,dp[p_3]*3,dp[p_5]*5)
     * p2,p3,p5分别是丑数序列的下标，用于递推丑数序列。由于丑数需要满足递增，所以
     * 更新序列时候，从p2,p3,p5指向的丑数中，分别乘以2，3，5，选取最小值作为更新，
     * 并将对应的下标自增，移动到下一个下标。
     *
     * 比如2的3倍和3的2倍，是否会形成重复?从指向1的下标开始，p2先
     */
    int dp(const int n) {
        vector<int> ugly(n);
        ugly[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for (int i = 1; i < n; ++i) {
            ugly[i] = min({2 * ugly[p2], 3 * ugly[p3], 5 * ugly[p5]});
            if (ugly[i] == 2 * ugly[p2]) ++p2;
            if (ugly[i] == 3 * ugly[p3]) ++p3;
            if (ugly[i] == 5 * ugly[p5]) ++p5;
        }
        return ugly.back();
    }
    
public:
    int nthUglyNumber(int n) {
        return dp(n);
    }
};