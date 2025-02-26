class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums 是一个序列，代表了一个数字。重新排列的 nums 中，找到比 nums 大的数中，最小的一个。
        即 nums 的下一趟相邻的值。比如 123456 的下一轮相邻较大值为 123465。

        需要关注把问题如何抽象表达。

        希望下一个数比当前数大，那么，需要将后面的大数与前面的小数交换，就能得到更大的数。
            1. 选择尽可能靠右侧部分交换。
            2. 找到尽可能小的大数，与前面小的数交换。比如 123465，下一次应当是 5 和 4 交换，而非 6 与 4 交换。
            3. 将大数换到前面后，大数后面所有数字要重置为升序，保证最小的排列。比如 123465，交换 5 和 4，得到 123564，
                将 5 后的数重置升数，即 123546，从而得到 1234XX 中，最小的值。
        关键在于步骤 2 的实现。从后向前查找第一个相邻升序元素对 (i,j)，满足 A[i] < A[j]，此时 [j, end) 比是降序。
        如果在步骤 1 找不到相邻元素对，说明当前列表式降序的，完全找不到相邻升序。

        """
