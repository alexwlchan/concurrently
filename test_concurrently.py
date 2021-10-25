from concurrently import concurrently

for input, output in concurrently(lambda x: x, range(100), max_concurrency=1):
    print(input, output)