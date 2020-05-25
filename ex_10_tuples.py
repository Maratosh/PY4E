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

