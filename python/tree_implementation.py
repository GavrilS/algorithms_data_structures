class Tree:

    def __init__(self, data, children=None):
        self.data = data
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)


    def add_child(self, node):
        try:
            assert isinstance(node, Tree)
            self.children.append(node)
        except AssertionError:
            print("Node is not a Tree construction!!!")

    def __repr__(self):
        return self.data


class BinaryTree:

    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        if left_child is not None:
            self.add_child_node(self.left_node, left_child)
        if right_child is not None:
            self.add_child_node(self.right_node, right_child)


    def add_child_node(self, node, child):
        try:
            assert isinstance(child, BinaryTree)
            node = child
        except AssertionError:
            print('Node is not a BinaryTree construction!!!')
    
    def __repr__(self):
        return self.data
