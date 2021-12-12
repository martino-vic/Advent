Today was the most difficult day so far. At first I thought this would be a task for the networkx package in Python. I spent 20 minutes searching for a solution or an Algorithm that was designed for this task, something like a Hamiltonian or a Euclidean path. After seing that networkx won't lead me anywhere I tried to visualise the problem on a piece of paper and drew down all the caves and their connections. Then listed up the first three paths I could find intuitively and was trying to abstract a pattern from that, but to no avail. I had a vague idea to work with dictionaries with cave-names as their keys and a list of connected caves as values. And then combine this somehow with a decision tree. After an hour I still haven't figured out the concept of how to solve this, so I checked the reddit solution section and surprisingly I found a piece of [code](https://topaz.github.io/paste/#XQAAAQCuBQAAAAAAAAA0m0pnuFI8c82uPD0wiI6r5tRSCrme8SokpTv9601K98sOENz1NnI6cB0i/X8PZloQgzFPggpjGXmGlnRinYUHA8R/guIY9NBL5JrxLyZFgXW531sHDfR8pBswAkShQIAcUehLVqULHt2BTtSsbeeAWDLZYdh60XIKg7FkmpQIW2R7zx2NPkIA8QdKx3eYH1sbkZtPIOHIZD8KnI3nfmxqZqIXgtqXxVpdX1PmE894vXKccgodvahjnP6s8AaqvjZ6xdqTUqSvhdfvcalkD9IcOdhHocdb1ITnzO6MCsZbvv3N4EKsjgJoJ9DARVSihxoZHBNPGQTGBkS4NiC5wQwQpRQNzMe6C5uQjmViqRMz9tZvjsx9EBEKeLLyoSR2KR5waE17V4GlHdpn+9LFvMrkuq7+vQgwFFJnbNtlm0ygYqh9DOgOfrmFDY4ub2hWC8h0nHgC9ZVhhlkVULC/rj9/Xzi19HeGuxXf0BxhuKuupZngArN8IcLVlrwqCj35ouldOn1LBvZf+J7YrPhvzRK/vaQt8sUgvNVezQjx1i3bHzlfOV1yGcoPAPwlzFhxudZhRgMo/P/NQP+9NNOP) that did its job right away. Its very readable straight forward code and yet I am somehow not fully able to grasp its functionality. New things learned here:  
Looping through list of lists:

```
>>> for a, b in [[1, 2], [3, 4], [5, 6]]:
>>>    print(a, b)
1 2
3 4
5 6
```
Appending to a list:

```
>>> a = [1, 2, 3]
>>> b = 4
>>> [*a, b]
[1, 2, 3, 4]
```
Another inetersting thing I observed is the usefulness of thinking in terms of stacks and push-down automata along with the frequent use of .pop()  