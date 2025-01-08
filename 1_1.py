class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self):
        self.start = None  # Указатель на начало списка

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next_node = self.start
        if self.start is not None:
            self.start.previous_node = new_node
        self.start = new_node

    def remove_from_front(self):
        if self.start is None:
            print("Список пуст, ничего удалять!")
            return None
        removed_value = self.start.value
        self.start = self.start.next_node
        if self.start is not None:
            self.start.previous_node = None
        return removed_value

    def find_node_at_position(self, pos):
        current_node = self.start
        current_index = 0
        while current_node is not None:
            if current_index == pos:
                return current_node
            current_node = current_node.next_node
            current_index += 1
        return None

    def append_list_at_position(self, another_list, pos):
        if pos < 0:
            print("Позиция не может быть отрицательной!")
            return

        if pos == 0:
            last_node_new_list = self._fetch_last_node(another_list)
            last_node_new_list.next_node = self.start
            if self.start:
                self.start.previous_node = last_node_new_list
            self.start = another_list.start
            return

        prior_node = self.find_node_at_position(pos - 1)
        if not prior_node:
            print("Нет такой позиции в списке!")
            return

        new_list_last_node = self._fetch_last_node(another_list)
        new_list_last_node.next_node = prior_node.next_node
        if prior_node.next_node:
            prior_node.next_node.previous_node = new_list_last_node

        prior_node.next_node = another_list.start
        if another_list.start:
            another_list.start.previous_node = prior_node

    def _fetch_last_node(self, linked_list):
        current = linked_list.start
        while current and current.next_node:
            current = current.next_node
        return current

    def display(self):
        current_node = self.start
        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.next_node
        print("None")


# Тестирование класса
primary_list = DoublyLinkedList()
primary_list.add_to_front(10)
primary_list.add_to_front(20)
primary_list.add_to_front(30)

print("Основной список после добавления элементов:")
primary_list.display()
print("Ожидание: 30 <-> 20 <-> 10 <-> None")

secondary_list = DoublyLinkedList()
secondary_list.add_to_front(60)
secondary_list.add_to_front(50)
secondary_list.add_to_front(40)

print("Второй список после добавления элементов:")
secondary_list.display()
print("Ожидание: 40 <-> 50 <-> 60 <-> None")

# Вставляем второй список в основной на указанную позицию 2
primary_list.append_list_at_position(secondary_list, 2)
print("Основной список после вставки второго:")
primary_list.display()
print("Ожидание: 30 <-> 20 <-> 40 <-> 50 <-> 60 <-> 10 <-> None")

# Удаляем элемент из начала основного списка (имитируем работу стека)
removed_element = primary_list.remove_from_front()
print(f"Удаленный элемент: {removed_element}")
print("Список после удаления элемента:")
primary_list.display()
print("Ожидание: 20 <-> 40 <-> 50 <-> 60 <-> 10 <-> None")

