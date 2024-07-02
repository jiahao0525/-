class TreeNode:
    def __init__(self, val):
        self.val = val        # 节点值
        self.sum = 0          # 节点左右子树和 (新树节点值)
        self.left = None       # 左子节点
        self.right = None      # 右子节点

inorder = []             # 中序遍历序列
preorder = []            # 前序遍历序列
indexMap = {}           # 记录中序序列中各值的位置 (处理重复值)

def main():
    global inorder, preorder, indexMap
    inorder = list(map(int, input().split()))   # 读取中序遍历序列
    preorder = list(map(int, input().split()))  # 读取前序遍历序列

    # 建立值到位置的映射 (处理重复值)
    for i, num in enumerate(inorder):
        indexMap.setdefault(num, []).append(i)

    # 构建原始二叉树
    root = build_tree(0, len(inorder) - 1, 0, len(preorder) - 1)

    # 中序遍历新二叉树 (输出结果)
    inorder_traversal(root)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)    # 遍历左子树
        print(root.sum, end=" ")        # 输出当前节点值 (左右子树和)
        inorder_traversal(root.right)   # 遍历右子树

def build_tree(in_start, in_end, pre_start, pre_end):
    if pre_start > pre_end:             # 子树为空 (递归终止条件)
        return None

    root_val = preorder[pre_start]     # 根节点值 (前序遍历首元素)
    root = TreeNode(root_val)          # 创建根节点

    # 找到根节点在中序遍历中的正确位置
    for idx in indexMap[root_val]:
        if in_start <= idx <= in_end:
            left_len = idx - in_start       # 左子树长度
            right_len = in_end - idx       # 右子树长度

            # 检查左右子树是否匹配 (避免错误位置)
            if not (not_equal(in_start, pre_start + 1, left_len) or
                    not_equal(idx + 1, pre_end - right_len + 1, right_len)):
                # 递归构建左右子树
                root.left = build_tree(in_start, idx - 1, pre_start + 1, pre_start + left_len)
                root.right = build_tree(idx + 1, in_end, pre_end - right_len + 1, pre_end)

                # 计算当前节点左右子树和 (新树节点值)
                root.sum = (root.left.val + root.left.sum if root.left else 0) + \
                           (root.right.val + root.right.sum if root.right else 0)
                break   # 找到正确位置后跳出循环

    return root

def not_equal(start1, start2, size):
    # 比较中序和前序子序列是否相等 (排序后比较)
    return sorted(inorder[start1:start1 + size]) != sorted(preorder[start2:start2 + size])

if __name__ == "__main__":
    main()


  
