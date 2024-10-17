def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    iterator = head
    resultList = ListNode(0)
    resultListIterator = resultList
    for _ in range(n):
        head = head.next
    while head != None:
        resultListIterator.next = iterator
        resultListIterator = resultListIterator.next
        iterator = iterator.next
        head = head.next
    resultListIterator.next = iterator.next
    return resultList.next