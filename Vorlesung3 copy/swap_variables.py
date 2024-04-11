>>> x = 42
>>> y = 10
>>> x = y
>>> y = x
>>> x
10
>>> y
10
>>> x = 42
>>> y = 10
>>> h = x
>>> x = y
>>> x
10
>>> y
10
>>> h
42
>>> y = h
>>> x
10
>>> y
42
>>> x, y = y, x
>>> x
42
>>> y
10
>>> y, x
(10, 42)
>>> type(y, x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
>>> type((y, x))
<class 'tuple'>