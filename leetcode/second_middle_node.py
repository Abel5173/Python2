import math

head = [int(i) for i in input().split()]

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
print(slow)