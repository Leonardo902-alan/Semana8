from collections import deque, defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def build_tree_from_list(self, values):
        if not values:
            return
        
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1


def vertical_order_traversal(root):
  
    if not root:
        return []
  
    node_map = defaultdict(list)

    queue = deque([(root, 0, 0)])  
    min_hd = max_hd = 0  
    
    while queue:
        node, hd, row = queue.popleft()
        
        if node:
           
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            node_map[hd].append((row, node.value))
            
            queue.append((node.left, hd - 1, row + 1))
            queue.append((node.right, hd + 1, row + 1))
    
    result = []
    for hd in range(min_hd, max_hd + 1):
       
        column = sorted(node_map[hd])
        result.append([value for _, value in column])
    
    return result


def test_vertical_order_traversal():
  
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
   
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    
    tree3 = BinaryTree()
    
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1])
 
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    
    result1 = vertical_order_traversal(tree1.root)
    result2 = vertical_order_traversal(tree2.root)
    result3 = vertical_order_traversal(tree3.root)
    result4 = vertical_order_traversal(tree4.root)
    result5 = vertical_order_traversal(tree5.root)
    
    print("Test Case 1: Normal binary tree")
    print(f"Result: {result1}")
    print("Expected: [[4], [2], [1, 5], [3], [6]]")
    
    print("\nTest Case 2: Vertical line tree")
    print(f"Result: {result2}")
    print("Expected: [[3], [2], [1]]")
    
    print("\nTest Case 3: Empty tree")
    print(f"Result: {result3}")
    print("Expected: []")
    
    print("\nTest Case 4: Single node tree")
    print(f"Result: {result4}")
    print("Expected: [[1]]")
    
    print("\nTest Case 5: Complete binary tree")
    print(f"Result: {result5}")
    print("Expected: [[4], [2], [1, 5, 6], [3], [7]]")
    
    assert result1 == [[4], [2], [1, 5], [3], [6]]
    assert result2 == [[3], [2], [1]]
    assert result3 == []
    assert result4 == [[1]]
    assert result5 == [[4], [2], [1, 5, 6], [3], [7]]
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_vertical_order_traversal()