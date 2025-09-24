import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphColoringApp:
    def __init__(self, root):
        self.root = root
        self.G = nx.Graph()
        self.NodeList = []
        self.sortedList = []
        self.defColor = "#1f78b4"

        self.Nodevar1 = StringVar(root, value="")
        self.Nodevar2 = StringVar(root, value="")

        self.color_palette = ["red", "green", "blue", "yellow"]
        self.pos = {}  # store node positions for stable layout

        self.build_ui()
        self.build_plot()

    def build_ui(self):
        top_frame = Frame(self.root)
        top_frame.pack(side=TOP, pady=10)

        Label(top_frame, text="Node 1:").grid(row=0, column=0)
        Entry(top_frame, textvariable=self.Nodevar1, width=10).grid(row=0, column=1)

        Label(top_frame, text="Node 2:").grid(row=0, column=2)
        Entry(top_frame, textvariable=self.Nodevar2, width=10).grid(row=0, column=3)

        Button(top_frame, text="Add", command=self.add_node).grid(row=0, column=4, padx=5)
        Button(top_frame, text="Color Graph", command=self.color_graph).grid(row=0, column=5, padx=5)

    def build_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def redraw(self, node_colors=None):
        self.ax.clear()
        if not self.G.nodes:
            self.canvas.draw()
            return

        if not self.pos:  # compute layout once
            self.pos = nx.spring_layout(self.G, seed=42)
        else:
            # assign positions for new nodes only
            new_nodes = set(self.G.nodes()) - set(self.pos.keys())
            if new_nodes:
                extra_pos = nx.spring_layout(self.G, seed=42)
                for n in new_nodes:
                    self.pos[n] = extra_pos[n]

        if node_colors is None:
            node_colors = [self.defColor] * len(self.G.nodes)

        nx.draw_networkx(self.G, ax=self.ax, node_color=node_colors,
                         nodelist=self.NodeList, pos=self.pos)
        self.canvas.draw()

    def add_node(self):
        n1, n2 = self.Nodevar1.get(), self.Nodevar2.get()
        if not n1 or not n2:
            return
        if n1 == n2:
            self.G.add_node(n1)
        else:
            self.G.add_edge(n1, n2)
        self.NodeList = list(self.G.nodes())
        self.redraw()

    def greedy_coloring(self):
        return nx.coloring.greedy_color(self.G, strategy="largest_first")

    def color_graph(self):
        if not self.G.nodes:
            return
        coloring = self.greedy_coloring()
        node_colors = []
        for node in self.NodeList:
            idx = coloring[node]
            if idx < len(self.color_palette):
                node_colors.append(self.color_palette[idx])
            else:
                node_colors.append("gray")
        self.redraw(node_colors)


root = Tk()
root.title("Graph Coloring App")
root.geometry("900x800")
app = GraphColoringApp(root)
root.mainloop()
