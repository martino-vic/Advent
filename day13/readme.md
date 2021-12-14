Today was the most challenging day. I spent four hours trying around, feeling I'm almost there. But eventually I didn't manage to get even a silver star. One intersting thing I learned:
```
>>> m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> m2 = [[0]*3]*3

>>> for i, j in zip([1],[1]):
>>>     m1[j][i] = 1

>>> for i, j in zip([1],[1]):
>>>     m2[j][i] = 1

>>> print(m1, m2)

[[0, 0, 0], [0, 1, 0], [0, 0, 0]] [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

```
If you create a matrix like this ```m2 = [[0]*3]*3``` for some reason an entire column will be inserted with ```m2[j][i] = 1```