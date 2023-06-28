class TreeHelper:

    def bt_dfs(self, tree):

        if tree:
            self.bt_dfs(tree.left_node)

            print(tree.data)

            self.bt_dfs(tree.right_node)
        
