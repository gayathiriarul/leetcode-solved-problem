class Solution:
    def sortedListToBST(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(arr[mid])

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(arr) - 1)
        