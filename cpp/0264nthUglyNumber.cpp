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
      for (int factor : {2, 3, 5}) {
        const long next = factor * num;
        if (!accounted.contains(next)) {
          accounted.insert(next);
          heap.push(next);
        }
      }
    }
    return ugly;
  }

 public:
  int nthUglyNumber(int n) { return minHeap(n); }
};