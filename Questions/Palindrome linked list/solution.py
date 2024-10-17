def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return True
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    rightPointer = slow.next
    is_even = fast.next is not None
    prev = None
    curr = head
    while curr != slow:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    if is_even:
        curr.next = prev
    else:
        curr = prev
    leftPointer = curr
    while leftPointer is not None:
        if leftPointer.val != rightPointer.val:
            return False
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next
    return True