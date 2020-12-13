class TreeNode:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


## 最大二叉树
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。


def max_tree(nums):
    if len(nums)  == 0:
        return None
    maxdata = -float('inf')
    maxdataIndex = -1
    for i, item in enumerate(nums):
        if item > maxdata:
            maxdata = item
            maxdataIndex = i
    root = TreeNode(maxdata)
    root.left = max_tree(nums[:maxdataIndex])
    root.right = max_tree(nums[maxdataIndex + 1:])
    return root



def traverse(root):
    if root is None:
        return
    print(root.item)
    traverse(root.left)
    traverse(root.right)


traverse(max_tree([3,2,1,6,0,5]))
