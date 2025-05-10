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
    
    def get_level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        while result and result[-1] is None:
            result.pop()
        
        return result


def serialize(root):
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    while result and result[-1] == "null":
        result.pop()
    
    return "[" + ",".join(result) + "]"


def deserialize(data):
    if data == "[]":
        return None
    
    values = data[1:-1].split(",")
    if not values or not values[0]:
        return None
    
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values):
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
        
        if i < len(values):
            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
    
    return root


def is_same_tree(p, q):
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.value != q.value:
        return False
    
    return (is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


def tree_to_list(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result


def test_serialize_deserialize():
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    
    tree2 = BinaryTree()
    
    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])
    
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    
    serialized1 = serialize(tree1.root)
    deserialized1 = deserialize(serialized1)
    
    serialized2 = serialize(tree2.root)
    deserialized2 = deserialize(serialized2)
    
    serialized3 = serialize(tree3.root)
    deserialized3 = deserialize(serialized3)
    
    serialized4 = serialize(tree4.root)
    deserialized4 = deserialize(serialized4)
    
    serialized5 = serialize(tree5.root)
    deserialized5 = deserialize(serialized5)
    
    print("Test Case 1: Normal binary tree 🌳")
    print(f"Original: {tree_to_list(tree1.root)}")
    print(f"Serialized: {serialized1}")
    print(f"Deserialized: {tree_to_list(deserialized1)}")
    print(f"Is same tree: {is_same_tree(tree1.root, deserialized1)}")
    
    print("\nTest Case 2: Empty tree 🈳")
    print(f"Original: {tree_to_list(tree2.root)}")
    print(f"Serialized: {serialized2}")
    print(f"Deserialized: {tree_to_list(deserialized2)}")
    print(f"Is same tree: {is_same_tree(tree2.root, deserialized2)}")
    
    print("\nTest Case 3: Single node tree 🌱")
    print(f"Original: {tree_to_list(tree3.root)}")
    print(f"Serialized: {serialized3}")
    print(f"Deserialized: {tree_to_list(deserialized3)}")
    print(f"Is same tree: {is_same_tree(tree3.root, deserialized3)}")
    
    print("\nTest Case 4: Left-skewed tree 📐⬅️")
    print(f"Original: {tree_to_list(tree4.root)}")
    print(f"Serialized: {serialized4}")
    print(f"Deserialized: {tree_to_list(deserialized4)}")
    print(f"Is same tree: {is_same_tree(tree4.root, deserialized4)}")
    
    print("\nTest Case 5: Right-skewed tree 📐➡️")
    print(f"Original: {tree_to_list(tree5.root)}")
    print(f"Serialized: {serialized5}")
    print(f"Deserialized: {tree_to_list(deserialized5)}")
    print(f"Is same tree: {is_same_tree(tree5.root, deserialized5)}")
    
    assert is_same_tree(tree1.root, deserialized1)
    assert is_same_tree(tree2.root, deserialized2)
    assert is_same_tree(tree3.root, deserialized3)
    assert is_same_tree(tree4.root, deserialized4)
    assert is_same_tree(tree5.root, deserialized5)
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_serialize_deserialize()