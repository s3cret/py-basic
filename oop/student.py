class student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Bad score") 

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

    def grade(self):
        print('%s: %s' % (self.__name, self.__score))
