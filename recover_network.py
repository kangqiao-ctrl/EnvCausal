from cdt.causality.graph import SAM
import networkx as nx
import torch

def recover_network(df):
	torch.multiprocessing.set_start_method('spawn', force=True)
    model = SAM(nruns=8)
    output = model1.predict(df)
    am = nx.adjacency_matrix(output).todense()
    return am