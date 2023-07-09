# Floyd Warshall Algorithm

The Floyd Warshall algorithm is also known as the All-Pairs Shortest Path (APSP) algorithm. It calculates the shortest paths between all the vertices in a weighted directed graph.

## Overview

The Floyd Warshall algorithm uses a dynamic programming approach to calculate the shortest distances between all pairs of vertices in a graph. It maintains a distance matrix that stores the shortest path distances between all pairs of vertices. The approach iteratively updates the distances by considering intermediate vertices, looking at the previouly calculated distances and minimizing the path distances.

## Features

- Finds out the shortest paths between all pairs of vertices.
- Supports positive as well as negative edge weights.
- Handles graphs with positive cycles but does not work properly with graphs that contain negative cycles.
- Detects negative cycles if available inside the graph.

## Usage

1. Make sure you have Python installed on you machine.
2. If you have git installed, you can simply clone the project. Or download the zip file from project directory.
3. the `main.py` file contains the the main function to run the project. Create a graph representation with edge weights.
4. Instantiate the Floyd-Warshall algorithm's object.
5. Call the `floyd_warshall` method on the algorithm object, passing your graph as input.
6. Retrieve the computed shortest distances or perform other operations based on your requirements.

```python
# Example usage in Python

from floyd_warshall import FloydWarshall

# Create a graph representation
graph = [[0, 5, float('inf'), 10],
         [float('inf'), 0, 3, float('inf')],
         [float('inf'), float('inf'), 0, 1],
         [float('inf'), float('inf'), float('inf'), 0]]

# Instantiate the Floyd-Warshall algorithm object
floyd_warshall = FloydWarshall()

# Compute the shortest distances
floyd_warshall.floydWarshall(graph)

# Access the computed shortest distances or perform other operations
```

## Performance

Floyd Warshall algorithm has a time complexity of O(V^3), where V is the number of vertices in the directed graph.

## Limitations

- The Floyd Warshall algorithm can not handle graphs having negative cycles.
- The space complexity of the algorithm is O(V^2) as it needs to store the distance matrix.
- It may not be efficient for large graphs with sparse connectivity.

## Contributions

I'm always open and would really appriciate if someone wants to make contributions to improve and enhance the project or provide additional features. If you encounter any issues or have suggestions regarding the project, please feel free to submit an issue or pull request.
