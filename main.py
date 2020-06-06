from collections import deque
import random, math, os
from graph_tool.all import *
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, GLib
import matplotlib.pyplot
import TarjanAlgorithm as Ta

state=None
win=None
B=[1, 1, 1, 1]

def update():
    win.graph.regenerate_surface()
    win.graph.queue_draw()
    return True

def createGraph():
    g = random_graph(50, lambda: (random.randint(0, 3), random.randint(0, 3)))
    g.set_directed(True)
    g = Graph(g, prune=True)
    pos=arf_layout(g)

    state = g.new_vertex_property("vector<double>")
    win = graph_draw(g, pos, vcmap=matplotlib,  vertex_fill_color=state, vertex_halo_color=[0, 0, 0, 1], main=update)
    return g

def main():
    g=createGraph()
    dict_graph={int(v):[] for v in g.get_vertices()}
    for i in range(len(g.get_edges())):
        node1=int(g.get_edges()[i][0])
        node2=int(g.get_edges()[i][1])
        dict_graph[node1].append(node2)
    graph=Ta.MathGraph(dict_graph)

    cc=Ta.getComponents(Ta.scc(graph))
    print("CONNECTED COMPONENTS: ", cc)

    # cid = GLib.idle_add(update())
    # win.connect("delete_event", Gtk.main_quit)
    # win.show_all()
    # Gtk.main()

if __name__=='__main__':
    main()
