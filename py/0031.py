class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums 是一个序列，代表了一个数字。重新排列的 nums 中，找到比 nums 大的数中，最小的一个。
        即 nums 的下一趟相邻的值。比如 1234*5**6* 的下一轮相邻较大值为 1234*6**5*。

        需要关注把问题如何抽象表达。

        希望下一个数比当前数大，那么，需要将后面的大数与前面的小数交换，就能得到更大的数。
            1. 选择尽可能靠右侧部分交换。
            2. 找到尽可能小的**大数**，与前面的**小数**交换。比如 123→4←6→5←，下一次应当是 5 和 4 交换，而非 6 与 4 交换。
            3. 将大数换到前面后，大数后面所有数字要重置为升序，保证最小的排列。比如 123465，交换 5 和 4，得到 123564，
                将 5 后的数重置升数，即 123546，从而得到 1234XX 中，最小的值。
        
        理解：
            尽可能小的**大数**，与前面的**小数**，具体定义为最靠右的相邻升序对，比如 (4,5)。注意不是 (4,6)，因此需要从右开始查找。

        实现找大数小数过程：
            1. 关键在于步骤 2 的实现。从后向前查找第一个**相邻**升序元素对 (i,j)，满足 A[i] < A[j]，此时 [j, end) 是降序。
                比如 {4,6} 和 {6,5}
            2. 在 [j, end) 从后向前查找**第一个** k，使其满足 A[i] < A[k]。A[i] 和 A[k] 对应上文的“小数”和“大数”。
            3. A[i] 和 A[k] 分别对应小数和大数，A[i] 与 A[k] 交换。
            4. 断定此时 [j, end) 必然降序，不会出现交换后打破降的情况。逆置 [j, end)，使其升序。
            5. 步骤 1 找不到相邻元素对，说明 [begin, end) 是单调降序的，所以直接跳到步骤 4
        """
        n = len(nums)
        if n <= 1:
            return
        i, j, k = n - 2, n - 1, n - 1

        # find A[i] < A[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0: # 不是最后一个排列
            # find A[i] < A[k]
            while nums[i] >= nums[k]:
                k -= 1
            # swap
            nums[i], nums[k] = nums[k], nums[i]
        
        i, j = j, n - 1
        # 反转 A[j:]，使 A[j:] 的值最小 
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1