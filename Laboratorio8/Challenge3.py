from collections import deque

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
            
            # Add left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1


def contains_node(root, value):

    if not root:
        return False
    
    if root.value == value:
        return True
    
    return contains_node(root.left, value) or contains_node(root.right, value)


def lowest_common_ancestor(root, p, q):
    if not root or not contains_node(root, p) or not contains_node(root, q):
        return None
    
    def find_lca(node, p, q):
        if not node:
            return None
        
        if node.value == p or node.value == q:
            return node
        
        left_lca = find_lca(node.left, p, q)
        right_lca = find_lca(node.right, p, q)
        
        if left_lca and right_lca:
            return node
        
        return left_lca if left_lca else right_lca
    
    lca_node = find_lca(root, p, q)
    
    return lca_node.value if lca_node else None


def test_lowest_common_ancestor():

    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])

    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])

    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
  
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5])
    
    lca1 = lowest_common_ancestor(tree1.root, 4, 6)
    lca2 = lowest_common_ancestor(tree2.root, 2, 4)
    lca3 = lowest_common_ancestor(tree3.root, 2, 3)
    lca4 = lowest_common_ancestor(tree4.root, 1, 3)
    lca5 = lowest_common_ancestor(tree5.root, 4, 7)  
    
    print("Test Case 1: Nodes in different subtrees")
    print(f"LCA of 4 and 6: {lca1}")
    print("Expected: 1")
    
    print("\nTest Case 2: One node is ancestor of other")
    print(f"LCA of 2 and 4: {lca2}")
    print("Expected: 2")
    
    print("\nTest Case 3: Nodes are siblings")
    print(f"LCA of 2 and 3: {lca3}")
    print("Expected: 1")
    
    print("\nTest Case 4: One node is the root")
    print(f"LCA of 1 and 3: {lca4}")
    print("Expected: 1")
    
    print("\nTest Case 5: Node not in tree")
    print(f"LCA of 4 and 7: {lca5}")
    print("Expected: None")
    
    assert lca1 == 1
    assert lca2 == 2
    assert lca3 == 1
    assert lca4 == 1
    assert lca5 is None
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_lowest_common_ancestor()