#!/usr/bin/env python
"""
This example does a "sleepy multiply".

It multiples two numbers together, but with a delay before returning.
This mimics a computation that has to be fetched from a remote server.

This example also shows how to handle functions that take multiple inputs.
"""

import time

from concurrently import concurrently


def sleepy_multiply(x, y):
    time.sleep(x / 10)
    return x * y


if __name__ == "__main__":
    inputs = [
        (1, 2),
        (2, 3),
        (7, 4),
        (3, 1),
        (5, 2),
        (4, 9),
        (7, 2),
        (6, 1),
    ]

    for (x, y), output in concurrently(lambda x: sleepy_multiply(*x), inputs=inputs):
        print(x, "*", y, "=", output)
