from queue import Queue


def myArray():

    arr = [10,20,30,40]
    return arr


def reverseArrayQueue(arr):
    #reverses an array using Queue.
    q = Queue()

    #enqueues all elements of the array into the queue
    for element in arr:
        q.put(element)

    #dequeue all elements and store them in the list
    reversedList = []
    while not q.empty():
        reversedList.insert(0, q.get())  # Insert at the beginning to reverse order

    return reversedList


if __name__ == "__main__":
    arr = myArray()  # Step 1: Takes array
    reversedArr = reverseArrayQueue(arr)  # Step 2: Reverse using Queue
    print("Reversed array:", *reversedArr)  # Step 3: Print output
