class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # checks for a head, if there is none, return head
    def mergeSort(self, head):
        if not head or not head.next:
            return head


    # sets middle
        middle = self.getMiddle(head)
        nextToMiddle = middle.next
        middle.next = None
    #sets left and right
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        return self.sortedMerge(left, right)
    # finds the middle
    def getMiddle(self, head):
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    # collects the sorted values
    def sortedMerge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

    def sort(self):
        self.head = self.mergeSort(self.head)
# finds avarage value of even numbers
    def averageEven(self):
        temp = self.head
        total, count = 0, 0
        while temp:
            if temp.data % 2 == 0:
                total += temp.data
                count += 1
            temp = temp.next
        return total / count if count else 0


# makes the inputed list
def inputList():
    sll = singlyLinkedList()
    list = [4, 2, 7, 1, 6, 3, 5]
    for num in list:
        sll.insert(num)
    return sll


# Print
sll = inputList()
print("Original List:")
sll.display()

sll.sort()
print("Sorted List:")
sll.display()

print("Average of Even Elements:", sll.averageEven())








