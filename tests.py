# import pytest
# from unittest.mock import patch
from app import App

INF = float('inf')

# @pytest.fixture
# def path():
#     return App()

def test_floyd_warshall():
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]
    expected_output = [
        [0, 5, 8, 9],
        [INF, 0, 3, 4],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    result = App(graph)
    assert result == expected_output

# def test_print_solution(capsys):
#     graph = [[0, 5, INF, 10],
#              [INF, 0, 3, INF],
#              [INF, INF, 0, 1],
#              [INF, INF, INF, 0]]
#     expected_output = "The following matrix shows the shortest distances between every pair of vertices\n" \
#                       "0 5 INF 10 \n" \
#                       "INF 0 3 INF \n" \
#                       "INF INF 0 1 \n" \
#                       "INF INF INF 0 \n"
#     App.print_solution(graph)
#     captured = capsys.readouterr()
#     assert captured.out == expected_output
