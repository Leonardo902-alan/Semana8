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
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    
    def to_list(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.value)
                if node.left or node.right: 
                    queue.append(node.left if node.left else None)
                    queue.append(node.right if node.right else None)
            else:
                result.append(None)
        
        while result and result[-1] is None:
            result.pop()
        
        return result


def prune_tree(root, target):

    if not root:
        return None
    
    root.left = prune_tree(root.left, target)
    root.right = prune_tree(root.right, target)
    
    if root.value == target:
        return root
   
    if not root.left and not root.right:
        return None

    return root


def tree_to_list(root):

    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.value)
            
            if node.left or node.right:
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result


def test_prune_tree():

    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])

    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(1)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.right = TreeNode(1)

    tree3 = BinaryTree()

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])

    tree5 = BinaryTree()
    tree5.root = TreeNode(5)
    tree5.root.left = TreeNode(5)
    tree5.root.right = TreeNode(5)

    original1 = tree_to_list(tree1.root)
    original2 = tree_to_list(tree2.root)
    original3 = tree_to_list(tree3.root)
    original4 = tree_to_list(tree4.root)
    original5 = tree_to_list(tree5.root)
    
    pruned1 = prune_tree(tree1.root, 1)
    pruned2 = prune_tree(tree2.root, 1)
    pruned3 = prune_tree(tree3.root, 1)
    pruned4 = prune_tree(tree4.root, 4)
    pruned5 = prune_tree(tree5.root, 5)
    
    pruned_list1 = tree_to_list(pruned1)
    pruned_list2 = tree_to_list(pruned2)
    pruned_list3 = tree_to_list(pruned3)
    pruned_list4 = tree_to_list(pruned4)
    pruned_list5 = tree_to_list(pruned5)
    
    print("Test Case 1: Normal binary tree, prune for value 1")
    print(f"Original: {original1}")
    print(f"Pruned: {pruned_list1}")
    print(f"Expected: [1]")
    
    print("\nTest Case 2: Tree with multiple occurrences of target")
    print(f"Original: {original2}")
    print(f"Pruned: {pruned_list2}")
    print(f"Expected: [1, 2, 3, 1, None, None, 1]")
    
    print("\nTest Case 3: Empty tree")
    print(f"Original: {original3}")
    print(f"Pruned: {pruned_list3}")
    print(f"Expected: []")
    
    print("\nTest Case 4: Target not in tree")
    print(f"Original: {original4}")
    print(f"Pruned: {pruned_list4}")
    print(f"Expected: []")
    
    print("\nTest Case 5: All nodes have target value")
    print(f"Original: {original5}")
    print(f"Pruned: {pruned_list5}")
    print(f"Expected: [5, 5, 5]")
    
    assert pruned_list1 == [1]
    assert pruned_list2 == [1, 2, 3, 1, None, None, 1]
    assert pruned_list3 == []
    assert pruned_list4 == []
    assert pruned_list5 == [5, 5, 5]
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_prune_tree()