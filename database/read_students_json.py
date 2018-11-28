'''read data from json file
'''
import json

class student():
    def __init__(self, name='default', score=0):
        self.name = name
        self.score = score

    def speak(self):
        print('My name is %s and my score is %d' % (self.name, self.score))

filename = 'students.json'
with open(filename, 'r') as f:
    content = f.read()
students_json = json.loads(content)
students_list = []
for each in students_json:
    name = each['name']
    score = each['score']
    students_list.append(student(name, score))
for each in students_list:
    each.speak()
