# --------------  Codecademy. -------------- #
#                                            #
#     PATH: Computer Science.                #
#     TRACK: Linear Data Structures.         #
#     LESSON: Nodes in Python.               #
#                                            #
# --------------  Codecademy. -------------- #


# New class `Node`.
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value


# New instances of `Node` class.
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Linking the nodes.
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# Getting values indirectly.
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

# Printing.
print(dots_data)
print(wackos_data)
