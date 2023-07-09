# import timeit

class App:
    
    def __init__(self, graph):
        self.graph = graph
        self.V = 4
        
    def floyd_warshall(self, graph):
        result = self.floyd_warshall_recursive(graph, self.V)
        return result
        # self.print_solution(result)

    def floyd_warshall_recursive(self, graph, n):
        if n == 1:
            return graph

        prev = self.floyd_warshall_recursive(graph, n - 1)
        curr = [[0] * self.V for _ in range(self.V)]

        for i in range(self.V):
            for j in range(self.V):
                curr[i][j] = min(prev[i][j], prev[i][n - 1] + prev[n - 1][j])

        return curr

    def print_solution(self, result):
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                print(result[i][j], end=" ")
            print()

