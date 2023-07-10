import pytest
from app import App

expected_output = """Following matrix shows the shortest distances between every pair of vertices
0 5 8 9
inf 0 3 4
inf inf 0 1
inf inf inf 0"""


@pytest.fixture
def graph():
    return [
        [0, 5, float("inf"), 10],
        [float("inf"), 0, 3, float("inf")],
        [float("inf"), float("inf"), 0, 1],
        [float("inf"), float("inf"), float("inf"), 0],
    ]


def test_floyd_warshall(graph, capsys):
    fw = App(graph)
    fw = fw.floyd_warshall(graph)

    # captured = capsys.readouterr()
    # output = captured.out.strip()
    # print(output)
    assert fw == [
        [0, 5, 8, 9],
        [float("inf"), 0, 3, 4],
        [float("inf"), float("inf"), 0, 1],
        [float("inf"), float("inf"), float("inf"), 0],
    ]
