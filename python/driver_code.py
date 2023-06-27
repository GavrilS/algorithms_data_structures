from tree_implementation import Tree

def main():
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
