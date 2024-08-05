import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def minimax(node, depth, is_maximizing_player):
    if len(node.children) == 0:
        return node.value

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def add_edges(graph, node, pos=None, level=0, width=2., vert_gap=0.4, xcenter=0.5):
    if pos is None:
        pos = {node: (xcenter, 1 - level * vert_gap)}
    else:
        pos[node] = (xcenter, 1 - level * vert_gap)

    neighbors = list(graph.neighbors(node))
    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos = add_edges(graph, neighbor, pos=pos, level=level + 1,
                            width=dx, xcenter=nextx)
    return pos

def draw_tree(root):
    G = nx.DiGraph()
    queue = [(root, None)]
    while queue:
        node, parent = queue.pop(0)
        if parent is not None:
            G.add_edge(parent, node)
        for child in node.children:
            queue.append((child, node))
            G.add_node(child)

    pos = add_edges(G, root)
    labels = {n: n.value for n in G.nodes}
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.show()

if __name__ == "__main__":
    root = TreeNode()
    child1 = TreeNode(value=None)
    child2 = TreeNode(value=None)
    child4 = TreeNode(value=9)
    child5 = TreeNode(value=0)
    child6 = TreeNode(value=7)
    child7 = TreeNode(value=8)

    root.children = [child1, child2]
    child1.children = [child4, child5]
    child2.children = [child6, child7]

    result = minimax(root, 0, True)
    root.value = result
    print("La meilleure évaluation pour le joueur maximisant est:", result)
    
    # Affichage de l'arbre
    draw_tree(root)

