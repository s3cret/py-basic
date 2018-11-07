# pickle.dump(object, file_descriptor) returns Nonetype
# pickle.dumps(object) returns bytes
# it is not the same thing that created from pickle.dumps and pickle.dump
import pickle
lst = [x * x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]
lst_dumps = pickle.dumps(lst)
print(lst_dumps)
with open('list_dumps.dp', 'wb') as f:
    print(type(pickle.dump(lst, f)))
