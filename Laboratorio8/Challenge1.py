class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def get_height(self):
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        if node is None:
            return 0
        
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_balanced(self):
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))


def balance_bst(tree):

    if tree.root is None:
        return BinarySearchTree()
    sorted_values = tree.inorder_traversal()
    
    balanced_tree = BinarySearchTree()
    balanced_tree.root = _build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)
    
    return balanced_tree


def _build_balanced_bst(sorted_values, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2
    root = Node(sorted_values[mid])
    
    root.left = _build_balanced_bst(sorted_values, start, mid - 1)
    root.right = _build_balanced_bst(sorted_values, mid + 1, end)
    
    return root


def test_balance_bst():
    """Test the balance_bst function. ⚖️"""
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)
    
    bst4 = BinarySearchTree()
    
    bst5 = BinarySearchTree()
    bst5.insert(42)
    
    balanced1 = balance_bst(bst1)
    balanced2 = balance_bst(bst2)
    balanced3 = balance_bst(bst3)
    balanced4 = balance_bst(bst4)
    balanced5 = balance_bst(bst5)
    
    assert bst1.inorder_traversal() == balanced1.inorder_traversal()
    assert bst2.inorder_traversal() == balanced2.inorder_traversal()
    assert bst3.inorder_traversal() == balanced3.inorder_traversal()
    assert bst4.inorder_traversal() == balanced4.inorder_traversal()
    assert bst5.inorder_traversal() == balanced5.inorder_traversal()
    
    assert balanced1.is_balanced()
    assert balanced2.is_balanced()
    assert balanced3.is_balanced()
    assert balanced4.is_balanced()
    assert balanced5.is_balanced()
    
    print("Test Case 1: Already balanced tree")
    print(f"Original height: {bst1.get_height()}, Balanced height: {balanced1.get_height()}")
    print(f"Original inorder: {bst1.inorder_traversal()}")
    print(f"Balanced inorder: {balanced1.inorder_traversal()}")
    print("Is balanced:", balanced1.is_balanced())
    
    print("\nTest Case 2: Right-skewed tree")
    print(f"Original height: {bst2.get_height()}, Balanced height: {balanced2.get_height()}")
    print(f"Original inorder: {bst2.inorder_traversal()}")
    print(f"Balanced inorder: {balanced2.inorder_traversal()}")
    print("Is balanced:", balanced2.is_balanced())
    
    print("\nTest Case 3: Left-skewed tree")
    print(f"Original height: {bst3.get_height()}, Balanced height: {balanced3.get_height()}")
    print(f"Original inorder: {bst3.inorder_traversal()}")
    print(f"Balanced inorder: {balanced3.inorder_traversal()}")
    print("Is balanced:", balanced3.is_balanced())
    
    print("\nTest Case 4: Empty tree")
    print(f"Original height: {bst4.get_height()}, Balanced height: {balanced4.get_height()}")
    print(f"Original inorder: {bst4.inorder_traversal()}")
    print(f"Balanced inorder: {balanced4.inorder_traversal()}")
    print("Is balanced:", balanced4.is_balanced())
    
    print("\nTest Case 5: Single node tree")
    print(f"Original height: {bst5.get_height()}, Balanced height: {balanced5.get_height()}")
    print(f"Original inorder: {bst5.inorder_traversal()}")
    print(f"Balanced inorder: {balanced5.inorder_traversal()}")
    print("Is balanced:", balanced5.is_balanced())
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_balance_bst()