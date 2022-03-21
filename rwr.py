from pyrwr.rwr import RWR


rwr = RWR()
rwr.read_graph("rmrA.txt", "undirected")
# r = rwr.compute(864, 0.75, 1e-9, 100)
r = rwr.compute(1688, 0.75, 1e-9, 100)


import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=1)
print(r)




out = open("rwroutA.txt",'w')
out.write(str(r))
out.close()



#jupyter notebook



# from pyrwr.rwr import RWR

# rwr = RWR()
# rwr.read_graph(input_graph, graph_type)
# r = rwr.compute(seed, c, epsilon, max_iters)

# Note that seed should be int. The format of the file at input_graph should follow one of the above input formats. r is a column vector (ndarray) having the RWR score vector w.r.t. seed node. The shape of r will be (n, 1) where n is the number of nodes.


# Arguments	Query Type	Explanation	Default
# query-type	common	Query type among [rwr, ppr, pagerank]	None
# graph-type	common	Graph type among [directed, undirected]	None
# input-path	common	Input path for a graph	None
# output-path	common	Output path for storing a query result	None
# seeds	rwr	A single seed node id	None
# seeds	ppr	File path for seeds (str) or list of seeds (list)	[]
# c	common	Restart probablity (rwr) or jumping probability (otherwise)	0.15
# epsilon	common	Error tolerance for power iteration	1e-9
# max-iters	common	Maximum number of iterations for power iteration	100
# handles_deadend	common	If true, handles the deadend issue	True
