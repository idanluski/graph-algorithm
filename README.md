# graph-algorithm
1 The company you work for produces a product that works on networks. Because half of your customers intend to run the
The product on regular networks, for the purpose of the simulations of the product, your boss asks you to produce for him
Random regular graphs.\
A. First, you must produce a graph with 10 = � 4-regular nodes (4 = �).\
B. Dotan, your team partner suggests you produce the graph in the following way:\
a. First, perform a random permutation on the nodes.\
b. Divide the nodes into 2 identical groups and form a circle from each group (total, 2 circles each circle contains
5 nodes (.\
c. Now connect each node in one circuit to another node in the second circuit (for example if the nodes of the circuits).\
They are (6,7,8,9,10),(1,2,3,4,5) so we will add to graph the arcs (5,10)...(2,7)(1,6) and get a graph
3-regular (.\
d. Now for 3 − � iterations: we will perform a cyclic permutation on one of the circuits and repeat the process
In section c) for example in the first iteration we will add the arcs (5,6)...(2,8)(1,7)(\
Irit, the second partner in the team, proposed a different solution:\
a. First, take 10 ⋅ 4 points.\
b. Divide the points into 10 groups of size 4 randomly.\
c. Make a pairing of the points (matching).\
d. Now combine each group of points into a single node (all arcs connected to one of the points in the group).\
become arcs connected to the node that represents the group).\
e. If the pairing does not contain arcs leaving and entering points from the same group, and does not contain two
arcs that connect the same groups, we got a 4-regular graph, otherwise, go back to section d.\
third. Explain in detail the complexities of the two algorithms from the proposals of the group members (on average and worst)
case, in relation to the number of nodes n and degree r).\
d. For each of the propositions, explain whether or not it is an algorithm for a uniform random regular graph,
and why? We emphasize that the algorithm must generate a regular graph randomly from among all regular graphs
the possible ones.\
God. Realize the algorithm(s) that you have decided is/are correct (correct i.e. that constitute
Algorithm for a uniform random regular graph among all possible regular graphs.\
and. Repeat section e for 9 times for the number of nodes 100...20,30,=n.\
G. Repeat sections d,e for 5,6,7,8=r (rank=r).\
H. For r, present a graph of the number of iterations (Y axis) as a function of the number of nodes (X axis) (total 5)
graphs (.\
ninth. For 100...20,40,60,=n present a graph of the amount of iterations (Y axis) as a function of the degree size (axis
X) (a total of 5 additional graphs)\
