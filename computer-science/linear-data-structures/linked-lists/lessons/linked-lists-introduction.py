# --------------- Codecademy. --------------- #
#                                             #
#     PATH: Computer Science.                 #
#     TRACK: Linear Data Structures.          #
#     LESSON: Linked Lists in Python.         #
#                                             #
# --------------- Codecademy. --------------- #


# New class `Node`.
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# New class `LinkedList`.
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        node_values = ""
        current_node = self.get_head_node()

        while True:
            node_values += str(current_node.value) + "\n"
            current_node = current_node.next_node

            if current_node.next_node is None:
                node_values += str(current_node.value) + "\n"
                break

        return node_values

    def remove_node(self, value_to_remove):
        current_node = self.head_node

        if current_node.value == value_to_remove:
            self.head_node = current_node.next_node
        else:
            while True:
                if current_node.next_node.value == value_to_remove:
                    current_node.set_next_node(current_node.next_node.get_next_node())
                    break
                else:
                    current_node = current_node.next_node


# Testing.
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)

print(ll.stringify_list())
