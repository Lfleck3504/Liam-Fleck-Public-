
def get_input():
    """Function to take input from the user."""
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    return s1, s2

def uncommonConcat(s1, s2):
    # Convert strings to sets to find unique characters
    set1 = set(s1)
    set2 = set(s2)
    # Find uncommon characters
    uncommonConcat= (set1 - set2) | (set2 - set1)
    # Convert the set to a sorted string
    result = ''.join(sorted(uncommonConcat))
    return result[::-1]


# Driver code to test the functions
s1, s2 = get_input()
output = uncommonConcat(s1, s2)
print("Output:",output)

