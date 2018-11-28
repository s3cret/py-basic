### SQLAlchemy
==============
Tables in database is a two-dimensional table, the data-structure can
be represented by python multi-line list, each list is consists of a
tuple representing column in table, which contains the each column's
data.
```python
[
    (1, 'Michael'),
    (2, 'Hack'),
    (3, 'Bob'),
    ...
]
```
It's hard to know the structure of the above data by a straight look.
If a tuple is represented by an instance of class, it will be nicer.

```python
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User(1, 'Michael'),
    User(2, 'Hack'),
    User(3, 'Bob'),
    ...
]
```
This is the so-called `Object-Relational-Mapping`, (ORM).

