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
