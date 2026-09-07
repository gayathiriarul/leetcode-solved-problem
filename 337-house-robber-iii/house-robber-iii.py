class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # Rob current house
            rob = node.val + left_skip + right_skip

            # Skip current house
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob, skip)

        rob, skip = dfs(root)

        return max(rob, skip)