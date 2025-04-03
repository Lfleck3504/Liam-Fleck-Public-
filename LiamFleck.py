
# Makes nodes for the tree
class TreeNode:
   def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None


#binary search tree is initialized
class BST:
   def __init__(self):
       self.root = None
   #makes an insert function to add to the tree
   def insert(self, value):
       if self.root is None:
           self.root = TreeNode(value)
       else:
           self.insertRecursive(self.root, value)


   # makes an insert recursive function
   def insertRecursive(self, node, value):
       if value < node.value:
           if node.left is None:
               node.left = TreeNode(value)
           else:
               self.insertRecursive(node.left, value)
       else:
           if node.right is None:
               node.right = TreeNode(value)
           else:
               self.insertRecursive(node.right, value)
   #sorts the tree into in order traversal form
   def inorderTraversal(self, node):
       if node is not None:
           self.inorderTraversal(node.left)
           print(node.value, end=" ")
           self.inorderTraversal(node.right)
   #finds the sums divisible by 5
   def sumDivisibleBy5(self, node):
       if node is None:
           return 0
       leftSum = self.sumDivisibleBy5(node.left)
       rightSum = self.sumDivisibleBy5(node.right)
       return leftSum + rightSum + (node.value if node.value % 5 == 0 else 0)


#main runing function that brings it all together
def main():
   bst = BST()


   # Taking user input for the tree
   values = list(map(int, input("Enter tree values (space-separated): ").split()))
   for val in values:
       bst.insert(val)


   print("\nIn-order Traversal of BST:")
   bst.inorderTraversal(bst.root)


   sumDiv5 = bst.sumDivisibleBy5(bst.root)
   print(f"\nSum of nodes divisible by 5: {sumDiv5}")
#executes the main function
if __name__ == "__main__":
   main()


