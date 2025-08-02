# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        serialized_list = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                serialized_list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized_list.append("null")
        # 末尾の余分な "null" を削除
        while serialized_list and serialized_list[-1] == "null":
            serialized_list.pop()
            
        return ",".join(serialized_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
          return None
        node_list = data.split(",")
        print(node_list)
        
        root = TreeNode(int(node_list[0]))
        node_queue = collections.deque([root])
        
        current_index = 1
        while node_queue and current_index < len(node_list):
          node = node_queue.popleft()
          if node_list[current_index] != "null":
            left = int(node_list[current_index])
            node.left = TreeNode(left)
            node_queue.append(node.left)
          current_index += 1
          if current_index < len(node_list) and node_list[current_index] != "null":
            right = int(node_list[current_index])
            node.right = TreeNode(right)
            node_queue.append(node.right)
          current_index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))