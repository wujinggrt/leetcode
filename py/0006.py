class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows 决定了旋转的 z 列方向有多少字母，而斜角方向有相同数量字母。
        # 每个全 z 有 2 * numRows + numRows - 2 个，numRows >= 2，
        # 半 z 有 numRows + numRows - 2 个
        # 一个旋转的 z 占用列一共  numRows 个，首位同时连接前后的 z
        # 可以遍历发现规律，考虑每个半 v，第一行就是开始的元素，第二行就是第二个和末尾，
        # 第三行是第三个和倒数第二个半 v 元素，依次类推
        # 特殊 case，numRows 为 2，第一个就是开始元素，第二个是末尾，不处理即可
        if numRows == 1:
            return s
        half = numRows + numRows - 2
        res = [" " for _ in range(len(s))]
        numZ = len(s) // half
        cursor = -1
        for i in range(numRows):
            # 第一行和最后一行仅仅选择对应下标的元素赋值
            # 中间行选择下标元素外，还选择对应位置的部分
            for j in range(numZ):
                cursor += 1
                res[cursor] = s[i + j * half]
                if i != 0 and i != (numRows - 1):
                    cursor += 1
                    res[cursor] = s[(j + 1) * half - i]
            forward = half * numZ + i
            if forward < len(s):
                cursor += 1
                res[cursor] = s[forward]
                back = half * (numZ + 1) - i
                if back < len(s) and back != forward:
                    # corner case: 不完整的 z 的竖的顶点，back 就是自己。
                    # 如果最后一个不完整的 z，只有竖的元素，那么会出现 back 为自己的情况
                    cursor += 1
                    res[cursor] = s[back]
        return "".join(res)

# 示例
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        down, up = True, False
        position = 0
        for char in s:
            result[position].append(char)
            if down:
                if position == numRows - 1:
                    position -= 1
                    down, up = up, down
                else:
                    position += 1
            else:
                if position == 0:
                    position += 1
                    down, up = up, down
                else:
                    position -= 1
        return "".join("".join(row) for row in result)