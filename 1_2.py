from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def combine_arrays(sorted_arr1, unsorted_arr2):  # объединение отсортированного массива с неотсортированным
    sorted_arr2 = sorted(unsorted_arr2)  # сортируем второй массив
    result = []
    i, j = 0, 0
    while i < len(sorted_arr1) and j < len(sorted_arr2):
        if sorted_arr1[i] <= sorted_arr2[j]:
            result.append(sorted_arr1[i])
            i += 1
        else:
            result.append(sorted_arr2[j])
            j += 1
    result.extend(sorted_arr1[i:])
    result.extend(sorted_arr2[j:])
    return result

def traverse_inorder(node, result=None):  # обходим дерево с записью элементов в массив
    if result is None:
        result = []
    if node is not None:
        traverse_inorder(node.left_child, result)
        result.append(node.value)
        traverse_inorder(node.right_child, result)
    return result

def add_to_bst(root, value):  # добавяем элемент в BST
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left_child = add_to_bst(root.left_child, value)
    elif value > root.value:
        root.right_child = add_to_bst(root.right_child, value)
    return root

def add_to_bt(tree, value):  # добавляем элемент в обычное бинарное дерево
    new_node = TreeNode(value)
    if not tree:
        return new_node
    queue = deque([tree])
    while queue:
        current = queue.popleft()
        if not current.left_child:
            current.left_child = new_node
            return tree
        else:
            queue.append(current.left_child)
        if not current.right_child:
            current.right_child = new_node
            return tree
        else:
            queue.append(current.right_child)
    return tree

def sorted_array_to_bst(arr):  # преобразуем отсортированный массив в сбалансированное бинарное дерево
    if not arr:
        return None
    mid_index = len(arr) // 2
    root = TreeNode(arr[mid_index])
    root.left_child = sorted_array_to_bst(arr[:mid_index])
    root.right_child = sorted_array_to_bst(arr[mid_index + 1:])
    return root

def remove_from_bst(root, value):  # удаление узла из BST
    if root is None:
        return root
    if value < root.value:
        root.left_child = remove_from_bst(root.left_child, value)
    elif value > root.value:
        root.right_child = remove_from_bst(root.right_child, value)
    else:
        if root.left_child is None:
            return root.right_child
        if root.right_child is None:
            return root.left_child
        smallest_right = get_min(root.right_child)
        root.value = smallest_right.value
        root.right_child = remove_from_bst(root.right_child, smallest_right.value)
    return root

def get_min(node):  # поиск мин элемента в дереве
    while node.left_child is not None:
        node = node.left_child
    return node

if __name__ == '__main__':
    tree1 = tree2 = None

    # Построение первого бинарного дерева поиска
    tree1 = add_to_bst(tree1, 45)
    tree1 = add_to_bst(tree1, 20)
    tree1 = add_to_bst(tree1, 70)
    tree1 = add_to_bst(tree1, 15)
    tree1 = add_to_bst(tree1, 30)
    tree1 = add_to_bst(tree1, 60)
    tree1 = add_to_bst(tree1, 90)
    
    bst_values = traverse_inorder(tree1)
    print('BST после вставки элементов:')
    print(' '.join(map(str, bst_values)))
    print("Ожидали вывод: 15 20 30 45 60 70 90")

    # Построение второго не отсортированного бинарного дерева
    tree2 = add_to_bt(tree2, 25)
    tree2 = add_to_bt(tree2, 10)
    tree2 = add_to_bt(tree2, 35)
    tree2 = add_to_bt(tree2, 5)
    tree2 = add_to_bt(tree2, 15)
    bt_values = traverse_inorder(tree2)
    print('BT после вставки элементов:')
    print(' '.join(map(str, bt_values)))
    print("Ожидали вывод: 5 10 15 25 35")

    # Слияние первого BST с элементами второго дерева
    bst_array = traverse_inorder(tree1)
    bt_array = traverse_inorder(tree2)
    merged_array = combine_arrays(bst_array, bt_array)
    merged_tree = sorted_array_to_bst(merged_array)
    
    result_values = traverse_inorder(merged_tree)
    print('BST после объединения с BT:')
    print(' '.join(map(str, result_values)))
    print("Ожидали вывод: 5 10 15 20 25 30 35 45 60 70 90")

    # Удаление нескольких узлов из объединенного дерева
    merged_tree = remove_from_bst(merged_tree, 10)
    merged_tree = remove_from_bst(merged_tree, 70)
    merged_tree = remove_from_bst(merged_tree, 90)
    
    final_values = traverse_inorder(merged_tree)
    print('BST после удаления элементов:')
    print(' '.join(map(str, final_values)))
    print("Ожидали вывод: 5 15 20 25 30 35 45 60")
