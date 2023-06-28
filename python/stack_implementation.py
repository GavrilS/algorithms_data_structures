class BasicStack:

    def __init__(self, item=None):
        self.stack = []
        if item is not None:
            self.stack.append(item)

    
    def add(self, item):
        self.stack.append(item)

    
    def pop(self):
        removed_item = self.stack[-1]
        # updated_stack = self.stack[:-1]
        # self.stack = updated_stack
        self.stack = self.stack[:-1]
        return removed_item

    
    def __repr__(self):
        return self.stack
