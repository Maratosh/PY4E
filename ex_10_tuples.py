''' DSU
#!Decorate
a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
#!Sort
the list of tuples using the Python built-in sort, and
#!Undecorate
by extracting the sorted elements of the sequence'''

txt = 'but soft  what light in yonder window breaks'
lst = [(len(word), word) for word in txt.split()]
lst.sort(reverse=True)
for l, w in lst:
    print(w, l)
#!Dictionaries and tuples


d = {'a':10, 'b':1, 'c':22}
lst = [(v, k) for k, v in list(d.items())]
lst.sort()
print(lst)                          #[(1, 'b'), (10, 'a'), (22, 'c')]

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d = {'a':10, 'b':1, 'c':22}
lst = [(v, k) for k, v in list(d.items())]
print(d)
d1 = {}             #{'a': 10, 'b': 1, 'c': 22}
for v, k in lst:
    d1[v] = k
print(d1)           #{10: 'a', 1: 'b', 22: 'c'}
