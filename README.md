# c2065064_csc1034_project3_2022 optimization report

## Load graph
For the load_graph function, I add a for loop method to add node and target to dictionary representing graph. Then, return the dictionary of lists since we can check if the nodes is in our dictionary as key or not.

## Print Stats
For this part, I first use two functions which is printEdges and printNodes. I also use generator expression to sum the number of edges instead a for loop. Method len() will count the number of keys in the graph dictionary which is the unique values. By doing return function, I reduce the number of lines compared to print function so the Python will stop the execution of the current function, sending a value out to where the function was called.

Here I put codes before implementing optimization method:
```
--
edges += len(targetURLs)
--
print("Nodes:", nodes) 
print("Edges:", edges)
--
```
## Stochastic Page Rank
I use dictionary of lists initially to find the difference in seconds with dictionary comprehension. It turns out dictionary of lists gives much faster results with 0.06 seconds in comparison to dictionary comprehension which gives 0.07 seconds even it have less code. But in the bottom result of 