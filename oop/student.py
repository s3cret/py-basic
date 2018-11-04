class Student(object):

    def __init__(self, name='default', score=0):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Bad score")

    def __str__(self):
        return 'Student object (name=%s, score=%d)' % (self.__name, self.score)

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'age':
            return 18

    def grade(self):
        print('%s: %s' % (self.__name, self.__score))
