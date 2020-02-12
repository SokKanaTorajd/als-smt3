class Node():
    def __init__(self,data):
        self.dataval = data
        self.next = None

head = None

#menambahkan node di depan
def AddFirst(node):
    global head
    node.next = head
    head = node

#menambahkan node di ujung
def AddLast(node):
    global head
    ujung = head
    while ujung.next:
        ujung = ujung.next
    ujung.next = nodeakhir

#menyisipkan node di tengah/setelah node awal
def InsertAt(NodeAwal,NodeBaru):
    global head
    NodeBaru.next = NodeAwal.next
    NodeAwal.next = NodeBaru

#menghapus node
def DeleteNode(NodeHapus):
    global head
    node = head
    if NodeHapus == node:
        #jika yang dihapus node pertama
        head = NodeHapus.next
    else:
        while not node.next == NodeHapus:
            node = node.next

def PrintNode():
    global head
    node = head
    print("======= print node =======")
    print(node.dataval)
    node = node.next
    print()

node1 = Node("node1")
AddFirst(node1)
PrintNode()

node2 = Node("node2")
AddFirst(node2)
PrintNode()

nodeakhir = Node("akhir")
AddLast(nodeakhir)
PrintNode()

nodebaru = Node("baru")
InsertAt(node1, nodebaru)
PrintNode()

# DeleteNode(node2)
# PrintNode()

node = head
while node is not None:
    print(node.dataval)
    node = node.next