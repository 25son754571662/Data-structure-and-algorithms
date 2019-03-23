# 返回构造的TreeNode根结点
def reConstructBinaryTree(self, pre, tin):
    #递归拆着做，截取左右子树的前序、中序序列
    #这就利用了python的优势了，二叉树的val不一定要保存成同一种形式
    if not pre or not tin:return None
    #根结点及其在后序序列中的index（对于先序序列，根节点一定是在首位）
    root,tin_index=TreeNode(pre[0]),tin.index(pre[0])
    #构造左、右子树
    root.left=reConstructBinaryTree(pre[1:tin_index+1],tin[0:tin_index])
    root.right=reConstructBinaryTree(pre[tin_index+1:],tin[tin_index+1:])
    return root