class Solution:
    def buildTree(self, inorder, postorder):
        index_map = {val: i for i, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            # root value from postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = index_map[root_val]

            # IMPORTANT: build right subtree first
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)
