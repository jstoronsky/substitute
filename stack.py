class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        next_node = self.top
        node = Node(data, next_node)
        self.top = node


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)  # 5
print(n2.data)  # a
print(n1)  # <__main__.Node object at 0x0000022803036050>
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.next_node.next_node.data)
