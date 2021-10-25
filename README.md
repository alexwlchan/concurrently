# concurrently

I often use the following pattern in Python:

```python
for task in get_tasks_to_do():
    perform(task)
```

Tasks run one after the other: task 1 runs to completion, then task 2 runs to completion, then task 3 runs to completion, and so on until everything is done.

This is fine for certain classes of task, but if `perform()` is heavily I/O bound, it's unnecessarily slow.
If I could run multiple instances of `perform()` concurrently, the overall process would complete much faster.
Task 1 could start, make a network request, then task 2 could start while task 1 is waiting.

I wrote [my recipe for concurrent processing][blog] in a blog post in 2019, but the code was a little cumbersome to use.
This repo is a tidied up (and tested!) version of that code.

It allows me to write code like:

```python
from concurrently import concurrently

for (input, output) in concurrently(fn=perform, inputs=get_tasks_to_do()):
    print(input, output)
```

It yields both the input and the output, because results may not come in the original order of inputs.

I would recommend using this code instead of the code in the original blog post.

[blog]: https://alexwlchan.net/2019/10/adventures-with-concurrent-futures/



## Usage

Copy and paste the file `concurrently.py` into your project.

You can see examples in the [`examples` directory](examples).



## License

MIT.
