from collections import deque
import random, math, os
from graph_tool.all import *
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, GLib
import matplotlib.pyplot

class MathGraph(object):
    def __init__(self, graph=None):
        if graph == None: graph = {}
        self.__graph = graph

    def get_nodes(self): return list(self.__graph.keys())

    def get_edges(self): return self.__generate_edges()

    def __generate_edges(self):
        edges = []
        for node in self.__graph:
            for adj in self.__graph[node]:
                if node!=adj: edges.append((node, adj))
        return edges

    def add_node(self, node):
        if node not in self.__graph: self.__graph[node] = []

    def add_edge(self, edge):
        if edge[0] in self.__graph: self.__graph[edge[0]].append(edge[1])
        else:self.__graph[edge[0]] = [edge[1]]

    def get_adj(self, node):
        adj=[]
        for edge in self.__generate_edges():
            if node==edge[0] and edge[0]!=edge[1]: adj.append(edge)
        return adj

def scc(graph):
    components_c=nodes_c=0
    # define the recursive function with the scope where the above variables are defined
    def dfs_scc(graph, node, connected_components, visited_nodes):
        nonlocal components_c, nodes_c # reference those variables
        nodes_c+=1
        connected_components[node]=-nodes_c
        visited_nodes.append(node)
        last=nodes_c
        for adj in graph.get_adj(node):
            if (connected_components[adj[1]]==0):
                b=dfs_scc(graph, adj[1], connected_components, visited_nodes)
                last=min(last, b)
            elif (connected_components[adj[1]]<0):
                last=min(last, -connected_components[adj[1]])
        if (last==-connected_components[node]):
            components_c+=1
            print('VISITED NODE QUEUE: ', list(visited_nodes), '; COMPONENTS COUNTER: ', components_c)
            while(visited_nodes[-1]!=node):
                w=visited_nodes.pop()
                connected_components[w]=components_c
            w=visited_nodes.pop()
            connected_components[w]=components_c
        return last
    #connected_components : {npde0: components, node1: components, node2: components, node3 : components, ...}
    connected_components={graph.get_nodes()[i]: 0 for i in range(len(graph.get_nodes()))}
    visited_nodes=deque()
    for node in graph.get_nodes():
        if (connected_components[node]==0):
            dfs_scc(graph, node, connected_components, visited_nodes)
    return connected_components
