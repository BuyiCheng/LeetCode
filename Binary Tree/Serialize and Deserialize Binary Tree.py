# _*_ coding: utf-8 _*_
"""
# @Time : 11/19/2021 9:30 AM
# @Author : byc
# @File : Serialize and Deserialize Binary Tree.py
# @Description :
"""


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

        def helper(root):
            if not root: return [None]
            s = [root.val]
            s += helper(root.left)
            s += helper(root.right)
            return s

        ss = ','.join([str(e) for e in helper(root)])
        return ss

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper():
            val = next(s_list)
            if val == 'None':
                return
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        s_list = iter(data.split(','))
        return helper()

#         def helper(data):

#             if data[0] == 'None':
#                 data.pop(0)
#                 return
#             node = TreeNode(data[0])
#             data.pop(0)
#             node.left = helper(data)
#             node.right = helper(data)
#             return node
#         s_list = data.split(',')
#         return helper(s_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))