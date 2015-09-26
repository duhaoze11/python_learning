import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def draw_graph() :
		G = nx.Graph()
		G.add_edges_from([(1, 2), (2, 3), (1, 3), (1, 4)])
		nx.draw(G)
		plt.savefig("simple_graph.png");

draw_graph()