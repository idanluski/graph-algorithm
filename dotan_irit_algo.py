import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random as rnd
import copy
from matplotlib.ticker import MaxNLocator


def dotan(n,r):
    G = nx.Graph()
    #fig = plt.figure()
    v = [i for i in range(1, n + 1)]

    # make permutation on v
    rnd.shuffle(v)

    # devide to two groups
    group_A = v[:len(v) // 2]
    group_B = v[len(v) // 2:]

    # making graph G
    G.add_nodes_from(v)

    # matching each group
    for i in range(len(group_A) - 1):
        G.add_edge(group_A[i], group_A[i + 1])
        G.add_edge(group_B[i], group_B[i + 1])
    G.add_edge(group_A[len(group_A) - 1], group_A[0])
    G.add_edge(group_B[len(group_B) - 1], group_B[0])

    # cyclic permutayion on group B r-3 times
    for i in range(0, r - 2):
        for j in range(len(group_A)):
            G.add_edge(group_A[j], group_B[(j + i) % len(group_A)])

    nx.draw_circular(G)
    plt.show(block = False)
    plt.savefig(r"C:\Users\luski\Desktop\grapg\homeworg1_graph\dotan_graph\v={0}_r= {1}_dotan.png".format(str(n), str(r)))
    plt.close()




def match(lst_dots,gr):
    """porpus: take r*n dots and find an matching for each dot that not inside a group of r dots
       return : empty list : if there is a copy of an edge or two dots from the same group
                list contain edges (represnt as set objects) If the pairing does not contain arcs
                 leaving and entering points from the same group, and does not contain two
                 arcs that connect those groups"""
    edges = []
    while (lst_dots):
        #taking randomly dots from groups and remove them
        a = rnd.choice(lst_dots)
        lst_dots.remove(a)
        b = rnd.choice(lst_dots)
        lst_dots.remove(b)
        idx_a=0
        idx_b =0
        for i in gr:
            # check if the dots in the same groups
            if (a in i) and (b in i):
                return []
            #
            if a in i:
                idx_a =gr.index(i)+1
            if b in i:
                idx_b =gr.index(i)+1
        if {idx_a,idx_b} in edges:
            return []
        edges.append({idx_a, idx_b})
    return edges

def irit(n,r):
    G = nx.Graph()
    #fig = plt.figure()
    dots = [i for i in range(1, r * n + 1)]  # generate a groups
    print(dots)
    rnd.shuffle(dots)  # shuffle a groups
    print(dots)
    dots_save = copy.deepcopy(dots)
    group = [dots[i:i + r] for i in range(0, (len(dots)), r)]  # devide a group to dots group size r
    lst_edge = match(dots, group)
    count = 1
    while (not (len(lst_edge))):
        count+=1
        lst_edge = []
        dots_s = copy.deepcopy(dots_save)
        lst_edge = match(dots_s, group)
    G = nx.Graph()
    v = [i for i in range(1, n + 1)]
    G.add_nodes_from(v)
    G.add_edges_from(lst_edge)
    print(count)
    # nx.draw_circular(G)
    #plt.show()
    #plt.show(block=False)
    #plt.savefig(r"C:\Users\luski\Desktop\grapg\homeworg1_graph\graph_irit\\n={0}_r= {1}_irit.png".format(str(n), str(r)))
    #plt.close()
    return count


r=4 #regularity
n=10 #verticies
ls_count =[]
ls_n = []


def plot_iteration_on_v():
    #fig = plt.figure()
    for r in range(4, 7):
        ls_n = []
        ls_count = []
        #median = []
        for n in range(10, 101, 10):
            #dotan(n,r)
            median = []
            for i in range(1, 11):
                median.append(irit(n, r))
            make_med = sum(median) / 10

            ls_n.append(n)
            ls_count.append(make_med)

        plt.plot(ls_n, ls_count, "-r")
        plt.xlabel("number of verticies")
        plt.ylabel("iteration")
        plt.title("r = " + str(r))
        plt.show(block=False)
        plt.savefig(r"C:\Users\luski\Desktop\grapg\homeworg1_graph\func graph\\n={0}_r= {1}_irit.png".format(str(n), str(r)))
        plt.close()


    #makin graph

def plot_iteration_on_r():
    fig = plt.figure()
    for n in range(20,101,20):
        ls_r = []
        ls_count = []

        for r in range(4,7):
            median = []
            for i in range(1, 6):
                median.append(irit(n, r))
            make_med = sum(median) / 10

            ls_r.append(r)
            ls_count.append(make_med)
        plt.plot([4,5,6], ls_count, "-r")
        plt.xlabel("regularity")
        plt.ylabel("iteration")
        plt.xticks([4,5,6])
        plt.title("n = " + str(n))
        plt.show(block=False)
        plt.savefig( r"C:\Users\luski\Desktop\grapg\homeworg1_graph\func graph\\n={0}_r= {1}_irit.png".format(str(n), str(r)))
        plt.close()
        #plt.show()



    #makin graph

#plot_iteration_on_r()
plot_iteration_on_r()

#print(lst_edge)
#nx.draw_circular(G)
#plt.show()

#dotan(10,5)












