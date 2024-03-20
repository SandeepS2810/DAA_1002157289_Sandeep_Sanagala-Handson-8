class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.s = [0] * cap
        self.top = -1

    def push(self, val):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.s[self.top] = val

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        val = self.s[self.top]
        self.top -= 1
        return val

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.cap - 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.s[self.top]


class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.q = [0] * cap
        self.front = self.rear = -1

    def enqueue(self, val):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.cap
        self.q[self.rear] = val

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.cap
        return val

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.cap == self.front


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def prepend(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def delete(self, val):
        if not self.head:
            print("List is empty")
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next
        print("Value not found")

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()


# Example:
s = Stack(5)
s.push(1)
s.push(6)
s.push(2)
s.push(3)
s.push(7)
s.push(8)  
print("Popped element:", s.pop())

q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)  
print("Dequeued element:", q.dequeue()) 

linked_l = SinglyLinkedList()
linked_l.append(1)
linked_l.append(2)
linked_l.prepend(0)
linked_l.display()  
linked_l.delete(1)
linked_l.display()  
