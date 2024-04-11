# region 링크드 리스트 생성
"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
# endregion

# region 링크드 리스트 순회
current = node1
while current is not None:
    print(current.data)
    current = current.next
# endregion"""


#스택 LIFO
'''stack = []
for i in range(1, 4):
    stack.append(i)
    print(stack[i-1])

#for i in range(0, 3):
print(stack.pop())'''

#큐 FIFO
'''from queue import Queue

queue = Queue()

for i in range(1, 4):
    queue.put(i)
    print(queue)

for i in range(0, 3):
    print(queue.get())'''

#트리
'''class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

preorder(root)'''

#그래프
'''graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(graph['A'])  # ['B', 'C']
print(graph['B'])  # ['A', 'D', 'E']
print(graph)
print(type(graph))
print(type(graph['A']))'''

#최갑근var 큐 예제

'''class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty:
            return self.items.pop(0)
        else:
            print("큐는 비어있습니다. dequeue를 수행할 수 없습니다.")
        
    def size(self):
        return len(self.items)

my_q = Queue()#Queue클래스에 대한 인스턴스 생성

for i in range(1, 4):
    my_q.enqueue(i)

print("큐 현재 상태 : ", my_q.items)

removed_item = my_q.dequeue()
print("remove item : ", removed_item)
print(my_q.items)
print("size : ", my_q.size())'''