class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertLast(a, x):
    tmp = Node(x)
    if a is None:
        a = tmp
    else:
        p = a
        while p.next is not None:
            p = p.next
        p.next = tmp

def deleteDuplicates(a):
    p = a
    while p is not None:
        truoc = p
        sau = p.next
        while sau is not None:
            if p.data == sau.data:
                truoc.next = sau.next
                sau = truoc.next
            else:
                truoc = sau
                sau = sau.next
        p = p.next

def printList(a):
    while a is not None:
        print(a.data, end=' ')
        a = a.next

head = None
n = int(input())
values = input().split()
for i in range(n):
    x = int(values[i])
    insertLast(head, x)

deleteDuplicates(head)
printList(head)
