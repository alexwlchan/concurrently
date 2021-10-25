import random
import time

from concurrently import concurrently


def double(x):
    time.sleep(random.random() / 100)
    return x * 2


def test_handles_iterator():
    result = set(concurrently(double, inputs=range(10)))

    assert result == {
        (0, 0),
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
        (5, 10),
        (6, 12),
        (7, 14),
        (8, 16),
        (9, 18),
    }


def test_handles_list():
    result = set(concurrently(double, inputs=[1, 3, 5, 7, 9, 11, 13]))

    assert result == {(1, 2), (3, 6), (5, 10), (7, 14), (9, 18), (11, 22), (13, 26)}
