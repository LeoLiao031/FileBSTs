import networkx as nx
import matplotlib.pyplot as plt
import csv

def build_tree_from_csv(filename):
    tree = nx.DiGraph()

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            parent = row[0]
            children = row[1:]

            for child in children:
                tree.add_edge(parent, child)

    return tree

def visualize_tree(tree):
    pos = nx.nx_pydot.graphviz_layout(tree, prog='dot')
    nx.draw(tree, pos, with_labels=True, node_size=1000, node_color="lightblue", alpha=0.7, font_weight="bold")
    plt.axis("off")
    plt.savefig("tree.png", format="PNG")
    plt.show()

# Read the CSV file and build the tree structure
filename = "data.csv"
tree = build_tree_from_csv(filename)

# Visualize the tree and save it as an image
visualize_tree(tree)
