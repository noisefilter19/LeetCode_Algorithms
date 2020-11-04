class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        stack = [[root]]
        serialized_data = [root.val]
        while stack:
            level = stack.pop()
            level = [(node.left, node.right) for node in level]
            level = [node for nodes in level for node in nodes]
            level_data = [node.val if node else None for node in level]
            level = [node for node in level if node]
            if not level:
                break
            serialized_data.extend(level_data)
            stack.append(level)
        return str(serialized_data)
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if data == "":
            return None
        data = list(data.split(','))
        index, num_nodes = 0, 0
        root = TreeNode(int(data[index]))
        cache = dict()
        cache[num_nodes] = root
        index += 1
        num_nodes += 1
        while index < len(data):
            if data[index].lstrip() == 'None':
                node = None
            else:
                node = TreeNode(int(data[index].lstrip()))
                cache[num_nodes] = node
                num_nodes += 1
            if index % 2 == 0:
                cache[(index-1)//2].right = node
            else:
                cache[(index-1)//2].left = node
            index += 1
        return cache[0]
