class Node():
    def __init__(self,data):
        self.dataval = data
        self.next = None

head = None

def AddFirst(node):
    global head
    node.next = head
    head = node

def AddLast(node):
    global head
    ujung = head
    while ujung.next:
        ujung = ujung.next
    ujung.next = nodeakhir

def newNode(day):
    days = Node(day)
    AddFirst(days)
    if AddLast(days) != None:
        AddLast(days)

hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]

for i in range(len(hari)):
    newNode(hari[i])
    i+1

node = head
while node is not None:
    print(node.dataval)
    node = node.next