import concurrent.futures
import itertools


def concurrently(fn, fn_inputs, *, max_concurrency=5):
    """
    Calls the function ``fn`` on the values ``inputs``.

    ``fn`` should be a function that takes a single input, which is the
    individual values in the iterable ``inputs``.

    Generates (input, output) tuples as the calls to ``fn`` complete.

    """
    fn_inputs = iter(fn_inputs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(fn, input): input
            for input in itertools.islice(fn_inputs, max_concurrency)
        }

        while futures:
            done, _ = concurrent.futures.wait(
                futures, return_when=concurrent.futures.FIRST_COMPLETED
            )

            for fut in done:
                original_input = futures.pop(fut)
                yield original_input, fut.result()

            for input in itertools.islice(fn_inputs, len(done)):
                fut = executor.submit(fn, input)
                futures[fut] = input


import time
import random

def doubler(input):
    print(f"Started {input}")
    time.sleep(random.randint(1, 10) / 100)
    print(f"Finished {input}")
    return input * 2


if __name__ == '__main__':
    for (input, output) in concurrently(doubler, range(10)):
        print(f"{input} ~> {output}")