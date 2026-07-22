# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        k %= n
        arr = arr[-k:] + arr[:-k]

        dummy = ListNode(0)
        cur = dummy
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next