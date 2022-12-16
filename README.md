# csc1034_project3_2022 optimization report {#c2065064}

## Load graph
For the load_graph function, I add a for loop method to add node and target to dictionary representing graph. The dictionary of lists should then be returned because we can determine if a node is a key in our dictionary or not. The dictionary can also be adjusted in accordance with this by switching the if statement to determine whether the node is not already a key.

## Print Stats
For this part, I first use two functions which is printEdges and printNodes. I also use generator expression to sum the number of edges instead a for loop. Method len() will count the number of keys in the graph dictionary which is the unique values. By doing return function, I reduce the number of lines compared to print function so the Python will stop the execution of the current function, sending a value out to where the function was called.
It turns out some part are missing and to avoid redundant lines of code, I decided to use for loop. I also try to make return functions to count number of edges and nodes respectively but it doesn't match with generator list which the number of nodes and edges is not printed. Hence, I use the built-in functions.
Here I put codes before implementing optimization method:
```
 yield targetURLs + len(targetURLs) # This is the same as doing edges = edges + len(targetURLs)

    return f"Nodes:", nodes , "Edges:", edges
```
## Stochastic Page Rank
I use dictionary of lists initially to find the difference in seconds with dictionary comprehension. It turns out dictionary of lists gives much faster results with 0.06 seconds in comparison to dictionary comprehension which gives 0.07 seconds even it have less code. But in the bottom result of it shows.

The initial dictionary comprehension is as follows:
```
nodes = list(graph.keys()) # Get all of our source nodes as a list
    hitcount = {node: 0 for node in nodes}

    for repetition in range(args.repeats):
    etc...
```

The second one is by import the `random` module at the start of python file. This can be made more efficient by instead doing `from random import choice` and the `current_node =  ̶r̶a̶n̶d̶o̶m̶.choice(nodes)` and `current_node =  ̶r̶a̶n̶d̶o̶m̶.choice(graph[current_node])` on the other loop nested inside repetitions loop which saves some time. current_node is now changed to be a different URL.It is selected at random from our current URL's target nodes. As our graph was saved as a dictionary of lists, this is possible. Calling graph[current node] provides a list of the URLs that our current position links to.

## Distribution Page Rank
The function runs at 0.20 seconds at first, as I implement dictionary comprehension, it increase by 0.01 seconds. This method is used the same as in stochastic page rank. I tried all lines by using dictionary comprehension and reduce the number of lines. By using this code below it takes around 0.07 seconds to calculate.
```

def distribution_page_rank(graph, args):

    nodes = list(graph.keys()) # Get all of our source nodes as a list
    node_prob = {} # Create an empty dictionary to store our nodes and overall probabilities
    for node in nodes:
        node_prob[node] = 1 / len(nodes) # Assign each node to the default probability value

    for step in range(args.steps):
        next_prob = {} # Create an empty dictionary to store our nodes and probabilities on a per-loop basis

        for node in nodes:
            next_prob[node] = 0 # Assign each node to a value of 0

```
Again, I'm assuming that the graph is implemented as a dictionary of lists, which is preferable, but I'm still testing dictionary comprehensions because they use less code and make the assumption that my computer runs more slowly. Our current node's value will be returned by graph[node]. The likelihood of a node being at the end increases with the number of times it appears in the dictionary's values. `next_prob[outURL] += p` means the out edges of a node are the URLs we could immediately leave to. `node_prob = next_prob` we are setting our overall probability dictionary to be our per-loop dictionary by overwriting the values.
## Overall optimization report

In overall, the calvulation for Stochastic is at 0.07 seconds while Distribution takes longer time which is 0.19 seconds. This can be explain by that we need to run many repetitions in order for these frequencies to accurately approximate probabilities. I executed the terminal to run the boilerplate code and replace some for loops. I also add import random to select random node. These method bit by bit reduce the amount of time needed and increase the performance. 