import sys
import os
import time
import argparse

from progress import Progress
from random import choice

def load_graph(args):
    """Load graph from text file

    Parameters:
    args -- arguments named tuple

    Returns:
    A dict mapling a URL (str) to a list of target URLs (str).
    """
    # Create empty dictionary to hold starting and target URLs
    graph_dict = {}
    # Iterate through the file line by line
    for line in args.datafile:
        # And split each line into two URLs
        node, target = line.split()

        if node in graph_dict.keys(): # Check if our current URL is in the current keys of our dictionary
            graph.dict[node].append(target) # If it is, append our current target to the existing values
        else:
            graph_dict[node] = [target] # If not, create a new key/value pair with our current node and target. The target is saved as a list so its values can be added to it later.

    file = open("school_web.txt")

    data = file.read()

    print(data)

    return graph_dict
    #raise RuntimeError("This function is not implemented yet.")

def print_stats(graph):

    nodes = len(graph)  # This will count the number of keys in the graph dictionary, i.e. the number of unique values
    edges = 0
    for targetURLs in graph.values():  # Loops through all the values in the dictionary, which are in this case lists, and adds the length of them to the 'edges' variables
        edges += len(targetURLs)

    print("Nodes:", nodes)
    print("Edges:", edges)

    """Print number of nodes and edges in the given graph"""

#raise RuntimeError("This function is not implemented yet.")

def stochastic_page_rank(graph, args):
    nodes = list(graph.keys()) # Get all of our source nodes as a list
    hitcount = {} # Create an empty dictionary to store our nodes and their hitcount

    for node in nodes: # Loop through every node. 'node' here stores a URL
        hitcount[node] = 0 # Add the node to the dictionary with a value of 0

    for repetition in range(args.repeats):
        current_node = random.choice(nodes) # Select a random node from all nodes, which we stored in the 'nodes' variable earlier

        for step in range(args.steps):
            current_node = random.choice(graph[current_node]) # Select a random node from the target nodes of our current URL

        hitcount[current_node] += 1 / args.repeats
    return hitcount


    """Stochastic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its hit frequency

    This function estimates the Page Rank by counting how frequently
    a random walk that starts on a random node will after n_steps end
    on each node of the given graph.
    """
    #raise RuntimeError("This function is not implemented yet.")


def distribution_page_rank(graph, args):
    nodes = list(graph.keys()) # Get all of our source nodes as a list
    node_prob = {} # Create an empty dictionary to store our nodesand overall probabilities
    for node in nodes:
        node_prob[node] = 1 / len(nodes) # Assign each node to the default probability value

    for step in range(args.steps):
        next_prob = {} # Create an empt dictionary to store our nodesand probabilities on a per-loop basis

        for node in nodes:
            next_prob[node] = 0 # Assign each node to a value of 0

        for node in nodes:
            targets = graph[node] # Get the target nodes of the current node
            p = node_prob[node] / len(targets) # Then calculate p basedon the current node's current overall probability


            for outURL in targets: # Loop through each URL in the targetsof our current node
                next_prob[outURL] += p # Update its probability in our per-loop dictionary

        node_prob = next_prob
    return node_prob

    """Probabilistic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its probability to be reached

    This function estimates the Page Rank by iteratively calculating
    the probability that a random walker is currently on any node.
    """

    #raise RuntimeError("This function is not implemented yet.")

parser = argparse.ArgumentParser(description="Estimates page ranks from link information")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Textfile of links among web pages as URL tuples")
parser.add_argument('-m', '--method', choices=('stochastic', 'distribution'), default='stochastic',
                    help="selected page rank algorithm")
parser.add_argument('-r', '--repeats', type=int, default=1_000, help="number of repetitions")
parser.add_argument('-s', '--steps', type=int, default=100, help="number of steps a walker takes")
parser.add_argument('-n', '--number', type=int, default=20, help="number of results shown")


if __name__ == '__main__':
    args = parser.parse_args()
    algorithm = distribution_page_rank if args.method == 'distribution' else stochastic_page_rank

    graph = load_graph(args)

    print_stats(graph)

    start = time.time()
    ranking = algorithm(graph, args)
    stop = time.time()
    time = stop - start

    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100*v:.2f}\t{k}' for k,v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")
