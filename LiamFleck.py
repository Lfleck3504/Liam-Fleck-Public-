# Function to take input from the user
def inputArray():
    arr = list(map(int, input("Enter space-separated integers: ").split()))
    return arr



# Function to reverse an array using a stack
def reverseUsingStack(arr):
    stack = []  # makes an empty stack

    # Pushes all the elements of the array arr into the stack
    for element in arr:
        stack.append(element)

    # Pop elements from the stack to reverse the array
    reversedArr = []
    while stack:
        reversedArr.append(stack.pop())

    return reversedArr


# Main driver function
if __name__ == "__main__":
    # Step 1: Get user input
    arr = inputArray()

    # Step 2: Reverse the array using a stack
    reversedArr = reverseUsingStack(arr)

    # Step 3: Print the reversed array
    print("Reversed Array:", " ".join(map(str, reversedArr)))
