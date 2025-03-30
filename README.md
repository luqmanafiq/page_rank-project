# CSC1034 PageRank Implementation Project

## Overview
This project implements and optimizes the PageRank algorithm for web page importance calculation using two different approaches:
1. Stochastic PageRank - Random walk simulation
2. Distribution PageRank - Iterative probability calculation

## Implementation Details

### Graph Structure
The web graph is represented as a dictionary of lists where:
- Each key is a source URL (node)
- Each value is a list of target URLs that the source URL links to

### Algorithm Implementations

#### Stochastic PageRank
This implementation estimates PageRank by simulating random walks on the graph:
- Start at a random node
- For a specified number of steps, randomly follow links
- Track the frequency each node is visited
- Node visit frequencies approximate their PageRank values

Optimization techniques:
- Used dictionary comprehension for initialization
- Imported `choice` directly from random module for performance
- Avoided redundant calculations by using direct random selection

#### Distribution PageRank
This implementation calculates PageRank by iteratively updating probability distributions:
- Initialize each node with equal probability (1/total nodes)
- For each step, redistribute probabilities based on link structure
- Final probabilities represent PageRank values

Optimization techniques:
- Used dictionary comprehension for initialization and step calculations
- Optimized loop structures to minimize redundant operations
- Used direct probability calculations instead of accumulating values

### Performance Comparison
- Stochastic PageRank: ~0.07 seconds (faster)
- Distribution PageRank: ~0.19 seconds (more precise)

The distribution method takes longer but provides more consistent results with fewer iterations, while the stochastic method requires many repetitions to accurately approximate probabilities.

## Usage Instructions

Run the script with a data file containing URL pairs:
```
python page_rank.py datafile.txt [options]
```

### Command Line Options
- `-m, --method`: Algorithm selection ('stochastic' or 'distribution')
- `-r, --repeats`: Number of repetitions for stochastic method (default: 1,000)
- `-s, --steps`: Number of steps in each walk/iteration (default: 100)
- `-n, --number`: Number of top results to display (default: 20)

### Example
```
python page_rank.py school_web.txt -m distribution -s 200
```

## Input File Format
The input file should contain pairs of URLs, where each pair represents a link from the first URL to the second URL:
```
http://source1.com http://target1.com
http://source1.com http://target2.com
http://source2.com http://target3.com
...
```

## Output
The program outputs:
1. Graph statistics (number of nodes and edges)
2. Top N pages ranked by their PageRank value
3. Calculation time

## Implementation Notes
- The implementation uses efficient data structures (dictionary of lists) for graph representation
- Dictionary comprehension is used for cleaner code but introduces a slight performance overhead
- Random selection is optimized by direct import of the `choice` function
