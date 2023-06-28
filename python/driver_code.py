from tree_implementation import Tree, BinaryTree
from stack_implementation import BasicStack
from tree_traversal import TreeHelper

def main():
    # test_general_tree()
    test_binary_tree()
    # test_stack()


def test_stack():
    stack = BasicStack(1)
    stack.add(2)
    stack.add(3)
    stack.add(4)
    stack.add(2)
    stack.add(5)
    print("Stack is: ", stack.__repr__())
    top_item = stack.pop()
    print("Removed from stack: ", top_item)
    print('Stack is: ', stack.__repr__())

def test_binary_tree():
    # bt = BinaryTree(
    #     'Root', 
    #     BinaryTree('Child1', 
    #         BinaryTree(
    #             'Child2', None, 
    #                 BinaryTree('Child4')), 
    #         BinaryTree('Child3')),
    #     BinaryTree('Child5', 
    #         BinaryTree('Child6'),
    #         BinaryTree('Child7'))
    # )
    
    bt = BinaryTree('Root')
    bt.left_node = BinaryTree('Child1')
    bt.left_node.left_node = BinaryTree('Child3')
    bt.left_node.right_node = BinaryTree('Child2')
    bt.right_node = BinaryTree('Child4')
    bt.right_node.left_node = BinaryTree('Child5')
    bt.right_node.right_node = BinaryTree('Child6')
    th = TreeHelper()
    th.bt_dfs(bt)




def test_general_tree():
    t = Tree(
        'Root', [
            Tree('Child1'),
            Tree('Child2'),
            Tree('Child3', [Tree('Child4'), Tree('Child5', [Tree('Child6')])])
        ]
    )
    print(t)
    print(t.children)
    for child in t.children:
        print(child)
        print(child.children)

if __name__=='__main__':
    main()