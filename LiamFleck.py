
def selectSort(arr):
    n = len(arr)

    for i in range(n - 1):   # Finds the maximum element
        maxNum = i
        for j in range(i + 1, n):
            if arr[j] > arr[maxNum]:

                maxNum = j

        arr[i], arr[maxNum] = arr[maxNum], arr[i]    # Swaps order
    return arr

#list
numbers = [2, 5, 3, 1, 4, 7, 6]

#list for even numbers
evenNumbers = []
for num in numbers:
    if num % 2 == 0: #identifies if its even
        evenNumbers.append(num)


# this finds the average value of even elements by deviding the total by the length of the list
def average(numbers):
    return sum(evenNumbers) / len(evenNumbers)

average = average(evenNumbers)

# this prints the list in decreasing order
sortedList = selectSort(numbers.copy())
print("Sorted List (decreasing):", sortedList)

#this prints the avarage of even elements
print("Average of Even Elements:", average)

#output
#Sorted List (decreasing): [7, 6, 5, 4, 3, 2, 1]
#Average of Even Elements: 4.0
