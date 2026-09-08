"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        all_nodes = {}
        all_nodes[node] = Node(node.val)
        q.append(node)
        while q:
            temp = q.popleft()
            for neighbor in temp.neighbors:
                if neighbor not in all_nodes:
                    all_nodes[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                all_nodes[temp].neighbors.append(all_nodes[neighbor])
                
        for key in all_nodes:
            return all_nodes[key]