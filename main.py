from collections import deque
import random, math, os
from graph_tool.all import *
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, GLib
import matplotlib.pyplot
import TarjanAlgorithm as Ta


def update():
    win.graph.regenerate_surface()
    win.graph.queue_draw()
    return True


def main():
    g={0: [1, 2], 1: [6], 2: [4], 3: [], 4: [5], 5: [2, 7], 6: [0], 7: []}
    graph=Ta.MathGraph(g)
    cc=Ta.scc(graph)
    print("CONNECTED COMPONENTS: ", cc)

    g = random_graph(100, lambda: (random.randint(0, 3), random.randint(0, 3)))
    g.set_directed(True)
    g = Graph(g, prune=True)
    pos=arf_layout(g)
    win = graph_draw(g, pos, vcmap=matplotlib, set_geometry=(900, 900))

    cid = GLib.idle_add(update())
    win.connect("delete_event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__=='__main__':
    main()
