import timeit
from app import App

if __name__ == "__main__":
    INF = float("inf")
    graph = [[0, 5, INF, 10], 
             [INF, 0, 3, INF], 
             [INF, INF, 0, 1], 
             [INF, INF, INF, 0]]

    fw = App(graph)
    result = fw.floyd_warshall(graph)
    print(result)

    # Performance testing:
    # Measure the execution time

    execution_time = timeit.timeit(lambda: fw.floyd_warshall(graph), number=1)
    print("Execution Time: ", execution_time)
